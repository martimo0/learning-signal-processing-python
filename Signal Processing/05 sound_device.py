import numpy as np
import sounddevice as sd
import time

# 1. Setup Parameters
s_rate = 44100
duration = 1.5
t = np.linspace(0, duration, int(s_rate * duration), endpoint=False)
freq = 220

# 2. Generate Waves

# Sine Wave
sin = 0.2 * np.sin(2 * np.pi * freq * t)

# Square Wave
sq = 0.05 * np.sign(np.sin(2 * np.pi * freq * t))

# Playback
print("Playing Pure Sine Wave (No harmonics - smooth)")
sd.play(sin, s_rate)
sd.wait()

time.sleep(0.5)

print("Playing Square Wave (Infinite Odd Harmonics - buzzing!)")
sd.play(sq, s_rate)
sd.wait()
print("Fin.")