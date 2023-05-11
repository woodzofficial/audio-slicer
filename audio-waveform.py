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

    plt.plot(time, audio_samples)
    plt.title("Audio WaveForm")
    plt.xlabel("Time/s")
    plt.ylabel("Value")
    plt.xlim(left=0)
    plt.ylim((-1, 1))
    plt.grid(True)
    plt.annotate("Slice #1", xy=(53, 1), xycoords=("data", "axes fraction"))
    plt.axvline(x=53, color='orange')
    plt.show()

if __name__ == "__main__":
    # showWaveForm("D:/测试/slicer测试音频/2009000334.wav")
    showWaveForm("D:/测试/slicer测试音频/Vocal (5).wav")