"""
03-instruments.py - Using custom instrument with events.

The default instrument ( DefaultInstrument ) is a basic stereo RC oscillator
passing through reverberation unit. For the events framework to be really
useful, it has to give the user the opportunity to use their own instruments.
Composing an instrument is very simple.

An Events's instrument must be derived from the EventInstrument class. Its
signature must be::

    class InstrumentName(EventInstrument):
        def __init__(self, **args):
            EventInstrument.__init__(self, **args)

The EventInstrument is responsible for the creation of the envelope, accessible
through the variable self.env, and also for clearing its resources when it's done
playing. 

All arguments given to the Events object can be retrieved in our instrument with 
the syntax self.argument_name (ex.: self.freq).

"""
from pyo import EventInstrument, SmoothDelay, Sig, Selector, Freeverb, Phasor, Expseg, ButLP, SfPlayer, Server, Events, EventSeq, EventChoice
from effects import EffectsUnit

class Instrument(EventInstrument):
    def __init__(self, **args):
        # print("Instrument Constructor")
        super().__init__(**args)
        self.osc = SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav", mul=self.env)
        # print("self.env: " + self.env)
        # self.filt = ButLP(self.osc, freq=5000)
        # self.delay = SmoothDelay(self.filt, delay=0.333, feedback=0.7)
        # self.delay_is_on = Sig(1)
        # self.delay_selector = Selector([self.osc, self.delay], self.delay_is_on) 
        # self.reverb_is_on = Sig(1)
        # self.reverb = Freeverb(self.delay_selector)
        # self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on).out()

class HiHat(EventInstrument):
    def __init__(self, **args):
        EventInstrument.__init__(self, **args)
        
        try:
            self.osc = SfPlayer("./samples/hihat/MA_CRLV_Hat_Closed_One_Shot_Zip.wav", mul=self.env, speed=self.sample_speed)
        except Exception as e:
            pass
        
        try:
            self.filt = ButLP(self.osc, freq=5000)
            self.delay = SmoothDelay(self.filt, delay=0.7, feedback=0.7)
            self.delay_selector = Selector([self.osc, self.delay], self.delay_is_on) 
            self.reverb = Freeverb(self.delay_selector)
            self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on).out()
        except Exception as e:
            pass
        
class Snare(Instrument):
    def __init__(self, **args):
        super().__init__(**args)
        self.sample_speed = 1.0
        self.osc = SfPlayer("./samples/snare/rhh_snare_one_shot_mid_short_old.wav", mul=self.env, speed=self.sample_speed)
        
        try:
            self.filt = ButLP(self.osc, freq=5000)
            self.delay = SmoothDelay(self.filt, delay=0.333, feedback=0.7)
            self.delay_selector = Selector([self.osc, self.delay], self.delay_is_on) 
            self.reverb = Freeverb(self.delay_selector)
            self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on).out()
        except Exception as e:
            pass

class Kick(Instrument):
    def __init__(self, **args):
        super().__init__(**args)
        self.sample_speed = 1.0
        self.osc = SfPlayer("./samples/kick/FL_LOFI_Kit09_Kick.wav", mul=self.env, speed=self.sample_speed)  
        
        try:
            self.filt = ButLP(self.osc, freq=5000)
            self.delay = SmoothDelay(self.filt, delay=0.333, feedback=0.7)
            self.delay_selector = Selector([self.osc, self.delay], self.delay_is_on) 
            self.reverb = Freeverb(self.delay_selector)
            self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on).out()
        except Exception as e:
            pass
