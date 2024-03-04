from pyo import EventInstrument, SmoothDelay, Sig, Selector, Freeverb, Phasor, Expseg, ButLP, SfPlayer, Server, Events, EventSeq, EventChoice

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
            self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on) # .out()
            self.mixer.addInput(0, self.reverb_selector)
            print(self.mixer)
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
            self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on) # .out()
            self.mixer.addInput(1, self.reverb_selector)
            print(self.mixer)
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
            self.reverb_selector = Selector([self.delay_selector, self.reverb], self.reverb_is_on) # .out()
            self.mixer.addInput(2, self.reverb_selector)
            print(self.mixer)
        except Exception as e:
            pass