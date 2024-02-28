from pyo import *

s = Server().boot()

class Metronome:
    def __init__(self, bpm=120):
        self.bpm = bpm
        self.metro = Metro(time=0.5, poly=1).play()
        self.freq = Sig(440)
        self.sine = Sine(self.freq, mul=0.5)

    def set_bpm(self, bpm):
        self.bpm = bpm
        self.metro.setTime(60.0 / self.bpm)

    def start_metronome(self):
        self.metro.play()

    def stop_metronome(self):
        self.metro.stop()

    def set_tempo(self, bpm):
        self.set_bpm(bpm)

    def start(self):
        self.metro.play()

    def stop(self):
        self.metro.stop()

    def set_frequency(self, freq):
        self.freq.setValue(freq)

# Create an instance of the Metronome class
metronome = Metronome()

# Set the initial BPM
metronome.set_bpm(120)

# Start the metronome
metronome.start()

# Infinite loop to allow user interaction
while True:
    try:
        bpm = float(input("Enter new BPM (0 to exit): "))
        if bpm == 0:
            break
        metronome.set_bpm(bpm)
    except ValueError:
        print("Invalid input. Please enter a number.")
        
s.start()