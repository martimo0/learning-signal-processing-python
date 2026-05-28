import numpy as np
import matplotlib.pyplot as plt
from scipy import signal # For Square + Sawtooth waves

# 1. SETUP PARAMETERS
s_rate = 1000
duration = 1.0
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)

# 2. GENERATE SIGNALS
sig1 = 1.5 * np.sin(2 * np.pi * 10 * t) # 10 Hz low frewq

sig2 = 0.6 * np.sin(2 * np.pi * 40 * t) # 40 Hz higher freq lower amplitude

comp = sig1 + sig2

square = signal.square(2 * np.pi * 5 * t)

saw = signal.sawtooth(2 * np.pi * 5 * t)

# 3. Plot it#

plt.figure(figsize=(12, 8))

# Plot 1: Composite signal breakdown
plt.subplot(3, 1, 1)
plt.plot(t, comp, label='Composite (10 Hz + 40 Hz)', color='purple', linewidth=2)
plt.plot(t, sig1, 'r--', alpha=0.5, label='10 Hz Component')
plt.title('Composite Signal in the Time Domain')
plt.xlabel('Time / s')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc='upper right')

# Plot 2: Square Wave (Digital/Synth Vibes)
plt.subplot(3, 1, 2)
plt.plot(t, square, label='5 Hz Square Wave', color='teal',)
plt.xlabel('Time / s')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc='upper right')

# Plot 3: Sawtooth Wave (Classical Synth Tone)
plt.subplot(3, 1, 3)
plt.plot(t, saw, label='5 Hz Sawtooth Wave', color='darkorange',)
plt.xlabel('Time / s')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()