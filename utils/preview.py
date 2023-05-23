import soundfile
import numpy as np
import matplotlib.pyplot as plt

from slicer2 import Slicer
from audioutil import AudioUtil

dark_theme_palette = {
    'primary': '#8ab4f7',
    'accent': 'orange',
    'page_background': '#202124',
    'figure_frame': '#404040',
    'figure_background': '#202020',
    'axis': '#A0A0A0',
    'title': '#e4e7eb',
    'grid': '#404040'
}
light_theme_palette = {
    'primary': '#1a73e8',
    'accent': 'orange',
    'page_background': '#f8f9fa',
    'figure_frame': '#B0B0B0',
    'figure_background': '#F0F0F0',
    'axis': '#505050',
    'title': '#4d5157',
    'grid': '#B0B0B0'
}


class SlicingPreview:
    def __init__(self,
                 filename: str,
                 sil_tags: list,
                 theme: str):
        self.filename = filename
        self.sil_tags = sil_tags
        self.theme = theme
        ori_audio, ori_sr = soundfile.read(filename, dtype=np.float32)

        # Convert to mono if not
        if len(ori_audio.shape) > 1:
            ori_audio = ori_audio.T
            ori_audio = AudioUtil.to_mono(ori_audio)

        # Downsample audio before plotting due to performance issue
        target_sr = 6000
        self.target_sr = target_sr
        self.audio_samples = AudioUtil.resample(y=ori_audio, orig_sr=ori_sr, target_sr=target_sr, res_type="soxr_hq")

    def _plot_preview(self, preview_filename: str):
        time = np.arange(0, len(self.audio_samples)) * (1.0 / self.target_sr)

        palette = dark_theme_palette if self.theme == 'dark' else light_theme_palette
        plt.rcParams['toolbar'] = 'None'
        plt.figure(figsize=(10, 6))

        # Plot Waveform
        plt.subplot(211)
        plt.plot(time, self.audio_samples, color=palette['primary'])
        fig = plt.gcf()
        fig.set_facecolor(palette['page_background'])
        fig.tight_layout(pad=3, w_pad=2, h_pad=3)
        ax = plt.gca()
        ax.set_facecolor(palette['figure_background'])
        ax.spines['top'].set_color(palette['figure_frame'])
        ax.spines['bottom'].set_color(palette['figure_frame'])
        ax.spines['left'].set_color(palette['figure_frame'])
        ax.spines['right'].set_color(palette['figure_frame'])
        ax.tick_params(
            axis='x',
            color=palette['axis'],
            labelcolor=palette['axis']
        )
        ax.tick_params(
            axis='y',
            color=palette['axis'],
            labelcolor=palette['axis']
        )
        plt.title(
            label='Audio WaveForm',
            fontdict={
                "color": palette['title']
            }
        )
        plt.xlabel(
            xlabel="Time/s",
            fontdict={
                "color": palette['axis']
            }
        )
        # plt.ylabel(
        #     ylabel="Value",
        #     fontdict={
        #         "color": palette['axis']
        #     }
        # )
        plt.grid(
            color=palette['grid']
        )
        plt.autoscale(enable=True, axis='x', tight=True)
        plt.ylim((-1, 1))
        for i in range(len(self.sil_tags)):
            start_pos = self.sil_tags[i][0] / self.target_sr
            end_pos = self.sil_tags[i][1] / self.target_sr
            plt.annotate("#" + i,
                         xy=(start_pos, 1),
                         xycoords=("data", "axes fraction"),
                         color=palette['accent']
                         )
            plt.axvline(x=start_pos, color=palette['accent'])
            plt.axvline(x=end_pos, color=palette['accent'])

        # Plot Length Distribution
        plt.subplot(223)
        plt.bar(["<2", "<5", "<8", "<11", "<14", "<17", "<20", ">=20"],
                [1, 5, 7, 11, 13, 7, 5, 1],
                color=palette['primary'])
        ax = plt.gca()
        ax.set_facecolor(palette['figure_background'])
        ax.spines['top'].set_color(palette['figure_frame'])
        ax.spines['bottom'].set_color(palette['figure_frame'])
        ax.spines['left'].set_color(palette['figure_frame'])
        ax.spines['right'].set_color(palette['figure_frame'])
        ax.tick_params(
            axis='x',
            color=palette['axis'],
            labelcolor=palette['axis']
        )
        ax.tick_params(
            axis='y',
            color=palette['axis'],
            labelcolor=palette['axis']
        )
        plt.title(
            label='Length Distribution',
            fontdict={
                "color": palette['title']
            }
        )

        # Plot Length Ranking List
        plt.subplot(224)
        plt.barh(["#5", "#1", "#6", "#8", "#12", "#7"], [21, 28, 32, 36, 45, 51], color=palette['primary'])
        ax = plt.gca()
        ax.set_facecolor(palette['figure_background'])
        ax.spines['top'].set_color(palette['figure_frame'])
        ax.spines['bottom'].set_color(palette['figure_frame'])
        ax.spines['left'].set_color(palette['figure_frame'])
        ax.spines['right'].set_color(palette['figure_frame'])
        ax.tick_params(
            axis='x',
            color=palette['axis'],
            labelcolor=palette['axis']
        )
        ax.tick_params(
            axis='y',
            color=palette['axis'],
            labelcolor=palette['axis']
        )
        plt.title(
            label='Length Ranking List',
            fontdict={
                "color": palette['title']
            }
        )
        plt.savefig(preview_filename, dpi=300)
        # plt.show()

    def save_plot(self, filename: str):
        self._plot_preview(filename)


def showWaveForm(filename):
    ori_audio, ori_sr = soundfile.read(filename, dtype=np.float32)
    if len(ori_audio.shape) > 1:
        ori_audio = ori_audio.T
        ori_audio = AudioUtil.to_mono(ori_audio)

    # Run slicer2 to get sli_tags
    slicer = Slicer(
        sr=ori_sr
    )
    sil_tags, total_frames = slicer.get_slice_tags(ori_audio)

    # Downsample audio before plotting due to performance issue
    target_sr = 6000
    audio_samples = AudioUtil.resample(y=ori_audio, orig_sr=ori_sr, target_sr=target_sr, res_type="soxr_hq")

    time = np.arange(0, len(audio_samples)) * (1.0 / target_sr)

    palette = dark_theme_palette
    plt.rcParams['toolbar'] = 'None'
    plt.figure(figsize=(10, 6))

    # Plot Waveform
    plt.subplot(211)
    plt.plot(time, audio_samples, color=palette['primary'])
    fig = plt.gcf()
    fig.set_facecolor(palette['page_background'])
    fig.tight_layout(pad=3, w_pad=2, h_pad=3)
    ax = plt.gca()
    ax.set_facecolor(palette['figure_background'])
    ax.spines['top'].set_color(palette['figure_frame'])
    ax.spines['bottom'].set_color(palette['figure_frame'])
    ax.spines['left'].set_color(palette['figure_frame'])
    ax.spines['right'].set_color(palette['figure_frame'])
    ax.tick_params(
        axis='x',
        color=palette['axis'],
        labelcolor=palette['axis']
    )
    ax.tick_params(
        axis='y',
        color=palette['axis'],
        labelcolor=palette['axis']
    )
    # plt.title(
    #     label='Audio WaveForm',
    #     fontdict={
    #         "color": palette['title']
    #     }
    # )
    plt.xlabel(
        xlabel="Time/s",
        fontdict={
            "color": palette['axis']
        }
    )
    # plt.ylabel(
    #     ylabel="Value",
    #     fontdict={
    #         "color": palette['axis']
    #     }
    # )
    plt.grid(
        color=palette['grid']
    )
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.ylim((-1, 1))
    # plt.annotate("#1",
    #              xy=(53, 1),
    #              xycoords=("data", "axes fraction"),
    #              color=palette['accent']
    #              )
    # plt.axvline(x=53, color=palette['accent'])
    # plt.axvline(x=65, color=palette['accent'])
    for i in range(len(sil_tags)):
        start_pos = sil_tags[i][0] / 1000. * 20
        end_pos = sil_tags[i][1] / 1000. * 20
        plt.annotate("#" + str(i + 1),
                     xy=(start_pos, 1),
                     xycoords=("data", "axes fraction"),
                     color=palette['accent']
                     )
        plt.axvline(x=start_pos, color=palette['accent'])
        plt.axvline(x=end_pos, color=palette['accent'])

    # Plot Length Distribution
    plt.subplot(223)
    plt.bar(["<2", "<5", "<8", "<11", "<14", "<17", "<20", ">=20"],
            [1, 5, 7, 11, 13, 7, 5, 1],
            color=palette['primary'])
    ax = plt.gca()
    ax.set_facecolor(palette['figure_background'])
    ax.spines['top'].set_color(palette['figure_frame'])
    ax.spines['bottom'].set_color(palette['figure_frame'])
    ax.spines['left'].set_color(palette['figure_frame'])
    ax.spines['right'].set_color(palette['figure_frame'])
    ax.tick_params(
        axis='x',
        color=palette['axis'],
        labelcolor=palette['axis']
    )
    ax.tick_params(
        axis='y',
        color=palette['axis'],
        labelcolor=palette['axis']
    )
    plt.title(
        label='Length Distribution',
        fontdict={
            "color": palette['title']
        }
    )

    # Plot Length Ranking List
    plt.subplot(224)
    plt.barh(["#5", "#1", "#6", "#8", "#12", "#7"], [21, 28, 32, 36, 45, 51], color=palette['primary'])
    ax = plt.gca()
    ax.set_facecolor(palette['figure_background'])
    ax.spines['top'].set_color(palette['figure_frame'])
    ax.spines['bottom'].set_color(palette['figure_frame'])
    ax.spines['left'].set_color(palette['figure_frame'])
    ax.spines['right'].set_color(palette['figure_frame'])
    ax.tick_params(
        axis='x',
        color=palette['axis'],
        labelcolor=palette['axis']
    )
    ax.tick_params(
        axis='y',
        color=palette['axis'],
        labelcolor=palette['axis']
    )
    plt.title(
        label='Length Ranking List',
        fontdict={
            "color": palette['title']
        }
    )
    # plt.savefig('preview.png', dpi=300)
    plt.show()


if __name__ == "__main__":
    # showWaveForm("D:/测试/slicer测试音频/2009000334.wav")
    showWaveForm("D:\\编曲学习\\小小\\小小（伊拾七干声）.wav")
    # showWaveForm("D:\\测试\\slicer测试音频\\Vocal (4).wav")
