import pyo
import wx

from sequencers import StepSeq, SeqManager

s = pyo.Server().boot()

s.recordOptions(filename = "./soudscape1.wav")
s.recstart()

def num_synths_slider_move(e):
    sm.set_num_voices(e.GetEventObject().GetValue())

def sf_speed_slider_move(e):
    audio_file.setSpeed(e.GetEventObject().GetValue() / 200)
    
def delay_time_slider_move(e):
    delay_time = e.GetEventObject().GetValue()
    sfdelay.setDelay(delay_time / 2000)
    # sfdelay.set(attr="delay", value=delay_time, port=0.1)
    # vsfdelay.delay = [delay_time, delay_time]

def event_0():
    sfdelay.setFeedback(0.99)
    print("event_0")
    
def event_1():
    print("event_1")
    sm.set_num_voices(1)
    
def event_2():
    print("event_2")
    sm.set_num_voices(3)
    
def event_3():
    print("event_3")
    audio_file.setSpeed(1.0)
    
def event_4():
    sfdelay.setFeedback(0.99)
    
def event_5():
    # sfdelay.setFeedback(0.3)
    pass

# note choices
harmonic_series = [100, 200, 300, 400, 500, 600, 700, 800]
whole_tone = pyo.midiToHz([60, 62, 64, 66, 68, 70, 72])
major = pyo.midiToHz([60, 62, 64, 65, 67, 69, 71, 72])
natural_minor = pyo.midiToHz([60, 62, 63, 65, 67, 68, 70, 72])
major_pent = pyo.midiToHz([60, 62, 64, 67, 69, 72])
minor_pent = pyo.midiToHz([60, 63, 65, 67, 70, 72])
       
sm = SeqManager()

audio_file = pyo.SfPlayer("./bamboo_chimes.wav", speed=-0.5, loop=True, mul=0.3)
audio_file.ctrl()

sfdelay = pyo.Delay(audio_file, delay=[1, 2], feedback=.5).out()
sfdelay.ctrl()

for i in range(0, 10):
    new_step_seq = StepSeq(natural_minor)
    sm.step_sequencers.append(new_step_seq)
    sm.synth_mixer.addInput(i, new_step_seq.filter)
    sm.synth_mixer.setAmp(i, 0, 0.07)
    sm.active_voices += 1

metro = pyo.Metro(4).play()
count = pyo.Counter(metro, min=0, max=8)
score = pyo.Score(count, fname="event_")

app = wx.App(False)

control_window = wx.Frame(None, wx.ID_ANY, "Soundscape 1")
control_window.Show(True)

num_synths_slider = wx.Slider(control_window, pos=wx.Point(0, 30), minValue=1, maxValue=10)
num_synths_slider.Bind(wx.EVT_SLIDER, num_synths_slider_move)
num_synths_slider_label = wx.StaticText(control_window, label="synth voices", pos=(10, 10))

sf_speed_slider = wx.Slider(control_window, pos=wx.Point(0, 70), minValue=-200, maxValue=200)
sf_speed_slider.Bind(wx.EVT_SLIDER, sf_speed_slider_move)
sf_speed_slider_label = wx.StaticText(control_window, label="soundfile speed", pos=(10, 50))

delay_time_slider = wx.Slider(control_window, pos=(0, 110), minValue=1, maxValue=2000)
delay_time_slider.Bind(wx.EVT_SLIDER, delay_time_slider_move)
delay_time_slider_label = wx.StaticText(control_window, label="delay time", pos=(10, 90))

s.start()
app.MainLoop()

s.recstop()

