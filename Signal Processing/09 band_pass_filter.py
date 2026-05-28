import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# 1. Setup Parameters and Generate Pure Gaussian Noise
s_rate = 12000
duration = 1.0
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)

# Pure Random Gaussian Noise
np.random.seed(42)
noise = np.random.normal(0, 1.0, size=len(t))

# 2. Define BPF Function
def butterBPF(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band', analog=False)
    return lfilter(b, a, data)

# Apply BPF
bpf = butterBPF(noise, lowcut=200, highcut=4800, fs=s_rate, order=6)

# 3. FFT Helper Function
def get_fft(signal, fs):
    n = len(signal)
    fft_vals = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]
    mags = (np.abs(fft_vals)/n)[:n//2] * 2
    return freqs, mags

freqs, pure_mag = get_fft(noise, s_rate)
_, bpf_mag = get_fft(bpf, s_rate)

# 4. Plot!
plt.figure(figsize=(14, 8))

# Row 1: Time Domain Comparison
#plt.subplot(2, 2, 1)
#plt.plot(t, noise, color='gray', alpha=0.5)
#plt.title('Original Noise (Time Domain)')
#plt.xlim(0, 0.05)
#plt.grid(True)

#plt.subplot(2, 2, 2)
#plt.plot(t, bpf, color='darkcyan')
#plt.title('Band-Pass Filtered Noise (Time Domain)')
#plt.xlim(0, 0.05)
#plt.grid(True)

# Row 2: Frequency Domain Comparison
#plt.subplot(2, 2, 3)
#plt.plot(freqs, pure_mag, color='gray', alpha=0.5)
#plt.title('Original Noise Specturm (0 to 6000 Hz)')
#plt.xlabel('Frequency / Hz')
#plt.grid(True)

#plt.subplot(2, 2, 4)
#plt.plot(freqs, bpf_mag, color='darkcyan')
# Draws red dashed lines at cutoff freqs
#plt.axvline(200, color='red', linestyle='--', label='200 Hz Cutoff')
#plt.axvline(4800, color='red', linestyle='--', label='4800 Hz Cutoff')
#plt.title('Band-Pass Specturm (Only 200 Hz - 4800 Hz Allowed)')
#plt.xlabel('Frequency / Hz')
#plt.legend()
#plt.grid(True)

#plt.tight_layout()
#plt.show()