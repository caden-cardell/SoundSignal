import numpy as np
import sounddevice as sd

# Parameters
fs = 44100  # Sample rate (Hz)
duration = 2.0  # Duration (seconds)
frequency = 440.0  # Tone frequency (Hz)
amplitude = 0.5  # Amplitude (0.0 to 1.0)
phase = np.pi / 2  # Phase in radians

# Generate time array
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Generate the waveform (sine wave)
signal = amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Play the sound
sd.play(signal, samplerate=fs)
sd.wait()  # Wait until the sound is done

# Play the sound
sd.play(signal, samplerate=fs / 2)
sd.wait()  # Wait until the sound is done