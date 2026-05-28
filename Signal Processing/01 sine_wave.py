import numpy as np
import matplotlib.pyplot as plt

# 1. Generate a time vector (1 second duration, sampled at 1 kHz)
s_rate = 1000
duration = 1.0
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)

# 2. Create a 5 Hz sine wave
freq = 5
signal = np.sin(2 * np.pi * freq * t)

# 3. Plot it
plt.figure(figsize=(10, 4))
plt.plot(t, signal, label ='5 Hz Sine Wave', color='blue')
plt.title('Signal Processing Test: Sine Wave')
plt.xlabel('Time / s')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
