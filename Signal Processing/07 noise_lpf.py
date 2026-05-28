import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# 1. Setup Parameters and Generate a Clean Signal
s_rate = 1000
duration = 1.0
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)
clean = 1.5 * np.sin(2 * np.pi * 10 * t) + 0.6 * np.sin(2 * np.pi * 40 * t)

# 2. Add White Noise
np.random.seed(42)
noise = np.random.normal(0, 0.8, size=len(t))
noisy = clean + noise

# 3. Design & Apply LPF
def butterLPF(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs # Nyquist's thereom dictates that freq is half the s_rate
    rcutoff = cutoff / nyquist
    # Get Filter Coefficients (b & a)
    b, a = butter(order, rcutoff, btype='low', analog=False)
    # Apply Filter
    y = lfilter(b, a, data)
    return y

cutoff_freq = 50
filtered_signal = butterLPF(noisy, cutoff_freq, s_rate, order=6)

# 4. FFT Helper Function
def get_FFT(signal, fs):
    n = len(signal)
    fft_vals = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n, 1/fs)[:n//2]
    mags = (np.abs(fft_vals)/n)[:n//2] * 2
    return freqs, mags

freqs, clean_mag = get_FFT(clean, s_rate)
_, noisy_mag = get_FFT(noisy, s_rate)
_, filtered_mag = get_FFT(filtered_signal, s_rate)

# 5. Plotting
plt.figure(figsize=(14, 10))

# Row 1: Time Domain Comparison
plt.subplot(3, 2, 1)
plt.plot(t, noisy, color='crimson')
plt.title('1. Noisy Signal (Time Domain)')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.plot(t, filtered_signal, color='forestgreen', linewidth=2)
plt.plot(t, clean, 'k--', alpha=0.5, label='Original Clean')
plt.title('2. Filtered Signal (Time Domain)')
plt.legend()
plt.grid(True)

# Row 2: Frequency Domain Comparison
plt.subplot(3, 2, 3)
plt.stem(freqs, noisy_mag, linefmt='4-', markerfmt='ro', basefmt=' ' )
plt.title('3. Noisy FFT (Frequency Domain)')
plt.xlim(0, 150)
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(freqs, filtered_mag, linefmt='g-', markerfmt='go', basefmt=' ')
plt.title('4. Filtered FFT (Frequency Domain)')
plt.xlim(0, 150)
plt.grid(True)

plt.tight_layout()
plt.show()