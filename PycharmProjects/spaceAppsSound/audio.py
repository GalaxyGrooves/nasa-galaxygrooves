import numpy as np
import sounddevice as sd
import time


# Define Note class
class Note:
    def __init__(self, duration, frequency, volume):
        self.duration = duration  # in seconds
        self.frequency = frequency  # in Hz
        self.volume = volume  # 0 to 1


# Initialize audio parameters
sample_rate = 44100  # Sample rate in Hz
sd.default.samplerate = sample_rate

# Create an array of Note objects
notes = [Note(0.5, 440, 0.5), Note(1, 880, 0.7), Note(0.2, 1760, 0.3)]

# Play the notes
for note in notes:
    # Generate time values
    t = np.linspace(0, note.duration, int(sample_rate * note.duration), endpoint=False)

    # Generate the sine wave signal
    x = note.volume * np.sin(2 * np.pi * note.frequency * t)

    # Play the sound
    sd.play(x, samplerate=sample_rate)

    # Wait until the sound is played completely
    sd.wait()

    # Pause between notes
    time.sleep(0.1)
