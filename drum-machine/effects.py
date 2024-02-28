from pyo import EventInstrument, SmoothDelay, Sig, Selector, Freeverb, Phasor, Expseg, ButLP, SfPlayer, Server, Events, EventSeq, EventChoice

class EffectsUnit():
    def __init__(self, sound_source):
        self.filt = ButLP(sound_source, freq=5000)
        self.delay = SmoothDelay(self.filt, delay=0.333, feedback=0.7)
        self.delay_is_on = Sig(0)
        self.delay_selector = Selector([sound_source, self.delay], self.delay_is_on) 
        self.reverb_is_on = Sig(1)
        self.reverb = Freeverb(self.delay_selector)
        self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on).out()