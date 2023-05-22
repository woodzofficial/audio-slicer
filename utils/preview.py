import soundfile
import numpy as np
import matplotlib.pyplot as plt


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


def showWaveForm(filename):
    audio_samples, sr = soundfile.read(filename, dtype=np.float32)
    is_mono = True
    if len(audio_samples.shape) > 1:
        is_mono = False
        audio_samples = audio_samples.T
    # if is_mono == False:
    # to mono
    time = np.arange(0, len(audio_samples)) * (1.0 / sr)

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
    plt.annotate("#1",
                 xy=(53, 1),
                 xycoords=("data", "axes fraction"),
                 color=palette['accent']
                 )
    plt.axvline(x=53, color=palette['accent'])
    plt.axvline(x=65, color=palette['accent'])

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
    plt.barh(["#5", "#1", "#6", "#8", "#12", "#7"],[21, 28, 32, 36, 45, 51], color=palette['primary'])
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
