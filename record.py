import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Parameters
fs = 44100  # Sample rate (Hz)
duration = 5.0  # Duration to record (seconds)

print("Recording...")

# Record audio for the specified duration
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')

# Wait until the recording is finished
sd.wait()

print("Recording finished!")

# Save the recording to a WAV file
wav.write("recording.wav", fs, recording)

print("Saved as 'recording.wav'")
