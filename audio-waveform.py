import soundfile
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def showWaveForm(filename):
    audio_samples, sr = soundfile.read(filename, dtype=np.float32)
    is_mono = True
    if len(audio_samples.shape) > 1:
        is_mono = False
        audio_samples = audio_samples.T
    # if is_mono == False:
    # to mono
    time = np.arange(0, len(audio_samples)) * (1.0 / sr)

    plt.rcParams['toolbar'] = 'None'
    plt.rcParams['axes.facecolor'] = '#202020'
    plt.figure(figsize=(10, 6))
    plt.plot(time, audio_samples, color='#8ab4f7')
    fig = plt.gcf()
    fig.set_facecolor("#202124")
    ax = plt.gca()
    ax.spines['top'].set_color('#404040')
    ax.spines['bottom'].set_color('#404040')
    ax.spines['left'].set_color('#404040')
    ax.spines['right'].set_color('#404040')
    ax.tick_params(
        axis='x',
        color='#A0A0A0',
        labelcolor='#A0A0A0'
    )
    ax.tick_params(
        axis='y',
        color='#A0A0A0',
        labelcolor='#A0A0A0',
    )
    plt.title(
        label='Audio WaveForm',
        fontdict={
            "color": "#e4e7eb"
        }
    )
    plt.xlabel(
        xlabel="Time/s",
        fontdict={
            "color": "#A0A0A0"
        }
    )
    # plt.ylabel(
    #     ylabel="Value",
    #     fontdict={
    #         "color": "#A0A0A0"
    #     }
    # )
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.ylim((-1, 1))
    plt.grid(
        color='#404040'
    )
    plt.annotate("Slice #1",
                 xy=(53, 1),
                 xycoords=("data", "axes fraction"),
                 color='orange'
                 )
    plt.axvline(x=53, color='orange')
    plt.show()


if __name__ == "__main__":
    # showWaveForm("D:/测试/slicer测试音频/2009000334.wav")
    showWaveForm("D:/测试/slicer测试音频/Vocal (5).wav")
