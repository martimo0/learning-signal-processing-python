import numpy as np
import matplotlib.pyplot as plt

# 1. Setup Parameters
s_rate = 1000
duration = 1.0
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)

# 2. Generate Signals
comp = 1.5 * np.sin(2 * np.pi * 10 * t) + 0.6 * np.sin(2 * np.pi * 40 * t)

# 3. Compute the Fourier Transform (Fast Fourier Transform)
n = len(comp)
fft_values = np.fft.fft(comp)
freqs = np.fft.fftfreq(n, 1/s_rate)

# 4. Post Processing
# The FFT returns complex numbers and we take the magnitude to get the Amplitude
# Also Normalise it by difiding by the number of samples (n)
mag = np.abs(fft_values) / n

# Since the FFT output is symmetrical, we only care about the positive half
half_n = n // 2
pos_freqs = freqs[:half_n]
pos_mag = mag[:half_n] * 2

# 5. Plotting Time Domain vs Frequency Domain
plt.figure(figsize=(12, 6))

# Plot 1: Time Domain (What we saw before)
plt.subplot(2, 1, 1)
plt.plot(t, comp, color='purple')
plt.title('Time Domain (What the signal looks like over time)')
plt.xlabel('Time / s')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot 2: Frequency Domain (The Fourier Transform)
plt.subplot(2, 1, 2)
plt.stem(pos_freqs, pos_mag, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Frequency Domain (The Fourier Tranform "Recipe")')
plt.xlabel('Frquency / Hz')
plt.ylabel('Amplitude')
plt.xlim(0, 60)
plt.grid(True)

plt.tight_layout()
plt.show()