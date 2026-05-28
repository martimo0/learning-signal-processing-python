import numpy as np
import matplotlib.pyplot as plt

# 1. Real World Continuous Signal
fs_cont = 2000
duration = 0.5
t_cont = np.linspace(0, duration, int(fs_cont * duration), endpoint=False)

freq = 40
cont = np.sin(2 * np.pi * freq * t_cont)

# 2. Good Sampling (Above Nyquist's: fs = 500 Hz)
fs_good = 500
t_good = np.linspace(0, duration, int(fs_good * duration), endpoint=False)
good = np.sin(2 * np.pi * freq * t_good)

# 3. Poor Sampling / Aliasing (Below Nyquist's: fs = 45 Hz)
# The required is 80 Hz making 45 Hz way below Nyquist's
fs_bad = 45
t_bad = np.linspace(0, duration, int(fs_bad * duration), endpoint=False)
bad = np.sin(2 * np.pi * freq * t_bad)

# 4. Plot!
plt.figure(figsize=(12, 7))

# Plot 1: Good Sampling
plt.subplot(2, 1, 1)
plt.plot(t_cont, cont, color='lightgray', label='True 40 Hz Signal')
plt.scatter(t_good, good, color='blue', s=20, label='Good Samples (500 Hz)')
plt.plot(t_good, good, 'b--', alpha=0.7, label='Reconstructed Wave')
plt.title('Good Sampling (Above Nyquists: Reconstructs 40 Hz Perfectly)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc='upper right')

# Plot 2: Bad Sampling (Aliasing)
plt.subplot(2, 1, 2)
plt.plot(t_cont, cont, color='lightgray', label='True 40 Hz Signal')
plt.scatter(t_bad, bad, color='crimson', s=50, label='Undersamples (45 Hz)')
# What the computah thinks the wave looks like based on the slow red dots
plt.plot(t_bad, bad, 'r-', linewidth=2, label='Fake "Alias" Wave')
plt.title('Bad Sampling (Below Nquist: Creates a Fake Low-Frequency Wave)')
plt.xlabel('Time / s')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()