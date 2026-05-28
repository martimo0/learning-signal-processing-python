import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Setup Parameters
s_rate = 44100
duration = 1.0
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)

# 2. Generate a 10 Hz Square Wave

freq = 10
square = signal.square(2 * np.pi * freq * t)

# 3. Compute FFT
n = len(square)
fft_values = np.fft.fft(square)
freqs = np.fft.fftfreq(n, 1/s_rate)

# Normalise and only look at +ve half
mag = np.abs(fft_values) / n
half_n = n // 2
pos_f = freqs[:half_n]
pos_m = mag[:half_n] * 2

# 4. Plot
plt.figure(figsize=(12, 6))

# Plot 1: Time Domain (The perfect Square steps)
plt.subplot(2, 1, 1)
plt.plot(t, square, color='teal', linewidth=2)
plt.title('Square Wave in the Time Domain')
plt.xlabel('Time / s')
plt.ylabel('Amplitude')
plt.ylim(-1.5, 1.5)
plt.grid(True)

# Plot 2: Frequency Domain (The Harmonic Ladder)
plt.subplot(2, 1, 2)
plt.stem(pos_f, pos_m, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Frequency Domain (THe infinite Odd Harmonics)')
plt.xlabel('Frequency / Hz')
plt.ylabel('Magnitude')
plt.xlim(0, 150)
plt.grid(True)

plt.tight_layout()
plt.show()