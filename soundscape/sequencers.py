from pyo import *

class StepSeq:
    def __init__(self, scale):
        self.filter_lfo = Sine(random.uniform(0.5, 20)).range(500, 2000)
        self.speed_lfo = Sine(random.uniform(0.5, 20)).range(1, 20)
        self.notes = scale
        self.random_note = Choice(self.notes, self.speed_lfo)
        self.synth = SuperSaw([self.random_note, self.random_note])
        self.filter = MoogLP(self.synth, self.filter_lfo)
        
class SeqManager:
    def __init__(self):
        self.step_sequencers = []
        self.active_voices = 0
        self.synth_mixer = Mixer(outs=3, chnls=2, time=0.5).out()
    
    def set_num_voices(self, num):
        i = self.active_voices - 1
        if num < self.active_voices - 1:  
            # print("if") 
            while i >= num:
                self.synth_mixer.setAmp(i, 0, 0)
                i -= 1
                self.active_voices -= 1    
        elif num > self.active_voices and num < 10:
            # print("elif")
            while i <= 9:
                # print("while")
                self.synth_mixer.setAmp(i, 0, 0.07)
                self.active_voices += 1
                i += 1