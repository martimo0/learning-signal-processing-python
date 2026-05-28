import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

# 1. Setup Parameters and get filter coefficients, a & b
s_rate = 12000
lowcut = 200
highcut = 4800

nyquist = 0.5 * s_rate
low = lowcut / nyquist
high = highcut / nyquist
b, a = butter(6, [low, high], btype='band', analog=False)

# 2. Define Logarithmic Decades for the sweep
# Sweeps from 10 Hz to 6000 Hz
start_decade = 1 # 10^1 = 10 Hz
end_decade = 4 # 10^4 = 10 kHz
total_decades = end_decade - start_decade

ppd = 100
total_points = total_decades * ppd

sweep_freq = np.logspace(start_decade, end_decade, num=total_points)
sweep_freq = sweep_freq[sweep_freq < nyquist]

_, response = freqz(b, a, worN=sweep_freq, fs=s_rate)

mag_dB = 20 * np.log10(np.abs(response))

# X. Plot!
plt.figure(figsize=(11, 6))

plt.semilogx(sweep_freq, mag_dB, color='darkcyan', linewidth=2, marker='o', markersize=4, label='Filter Response')


plt.axvline(200, color='red', linestyle='--', label='200 Hz Cutoff')
plt.axvline(4800, color='red', linestyle='--', label='4800 Hz Cutoff')

plt.title('AC Sweep: Logarithmic Bode Plot (10 Points per Decade)')
plt.xlabel('Frequency / Hz (Logarithmic)')
plt.ylabel('Magnitude / dB')

plt.grid(True, which='both', linestyle=':', alpha=0.6)
plt.ylim(-60, 5)
plt.legend()
plt.tight_layout()
plt.show()