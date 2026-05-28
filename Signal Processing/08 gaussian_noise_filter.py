import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# 1. Setup Parameters and Generate Pure Gaussian Noise
s_rate = 2000
duration = 1.0
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)

# Pure Random Gaussian Noise
np.random.seed(42)
noise = np.random.normal(0, 1.0, size=len(t))

# 2. Define Filter Functions
def butter_filter(data, cutoff, fs, btype, order=5):
    nyquist = 0.5 * fs
    rcutoff = cutoff / nyquist
    b, a = butter(order, rcutoff, btype=btype, analog=False)
    return lfilter(b,a, data)

# LPF at 150 Hz
lpf = butter_filter(noise, cutoff=150, fs = s_rate, btype='low', order=6)

# HPF at 700 Hz
hpf = butter_filter(noise, cutoff=700, fs = s_rate, btype='high', order=6)

# 3. FFT Helper Function
def get_fft(signal, fs):
    n = len(signal)
    fft_vals = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]
    mags = (np.abs(fft_vals)/n)[:n//2] * 2
    return freqs, mags

freqs, pure_mag = get_fft(noise, s_rate)
_, lpf_mag = get_fft(lpf, s_rate)
_, hpf_mag = get_fft(hpf, s_rate)

# 4. Plot!
plt.figure(figsize=(15, 10))

# Column 1: Time Domain
plt.subplot(3, 2, 1)
plt.plot(t, noise, color='gray', alpha=0.7)
plt.title('Original White Noise (Time Domain)')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.plot(t, lpf, color='blue')
plt.title('Low-Pass Filtered (Smoothed Out)')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.plot(t, hpf, color='purple',)
plt.title('High-Pass Filtered (Spiky/Jittery)')
plt.xlabel('Time / s')
plt.grid(True)

# Column 2: Frequency Domain

plt.subplot(3, 2, 2)
plt.plot(freqs, pure_mag, color='gray', alpha=0.7)
plt.title('Original White Spectrum (All Frequencies Equal))')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(freqs, lpf_mag, color='blue')
plt.axvline(150, color='red', linestyle='--', label='150 Hz Cutoff')
plt.title('Low-Pass Filtered (Highs Removed)')
plt.legend()
plt.grid(True)

plt.subplot(3, 2, 6)
plt.plot(freqs, hpf_mag, color='purple',)
plt.axvline(700, color='red', linestyle='--', label='700 Hz Cutoff')
plt.title('High-Pass Specturm (Lows Removed)')
plt.xlabel('Frequency / Hz')
plt.grid(True)

plt.tight_layout()
plt.show()