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

    palette = light_theme_palette
    plt.rcParams['toolbar'] = 'None'
    plt.figure(figsize=(10, 6))
    plt.plot(time, audio_samples, color=palette['primary'])
    fig = plt.gcf()
    fig.set_facecolor(palette['page_background'])
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
    plt.annotate("Slice #1",
                 xy=(53, 1),
                 xycoords=("data", "axes fraction"),
                 color=palette['accent']
                 )
    plt.axvline(x=53, color=palette['accent'])
    plt.show()


if __name__ == "__main__":
    # showWaveForm("D:/测试/slicer测试音频/2009000334.wav")
    showWaveForm("D:\\编曲学习\\眉间雪\\眉间雪-1-洛天依.wav")
