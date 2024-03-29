from pyo import EventSeq
from threading import Thread

def set_bpm(bpm, instruments):
    def set(instrument):
        instrument["bpm"] = bpm

    threads = [Thread(target=set, args=(instr,)) for instr in instruments]
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
        
def set_main_volume():
    pass

def set_subdivision(time, instrument):
    instrument["beat"] = EventSeq([1 / time])
    
def set_sample_speed(tuning, instrument):
    instrument["tuning"] = EventSeq([tuning])

def toggle_reverb(button, instrument):
    # print(button)
    current_color = button.cget("fg_color")
    # print(instrument["effects"])
    # print(instrument)
    if current_color == "black":
        instrument["reverb_is_on"].setValue(1)
        button.configure(fg_color="green")
        #instrument.instr.effects.reverb_is_on = 1
    else:
        instrument["reverb_is_on"].setValue(0)
        button.configure(fg_color="black")
        # instrument.instr.effects.reverb_is_on = 0
    
def toggle_delay(button, instrument):
    # print(instrument)
    current_color = button.cget("fg_color")
    if current_color == "black":
        button.configure(fg_color="green")
        instrument["delay_is_on"].setValue(1)
    else:
        button.configure(fg_color="black")
        instrument["delay_is_on"].setValue(0)
        
def toggle_sequencer_step(button, instrument):
    # print(instrument)
    current_color = button.cget("fg_color")
    if current_color == "black":
        button.configure(fg_color="purple")
        instrument["volume"].setValue(1)
    else:
        button.configure(fg_color="purple")
        instrument["volume"].setValue(0)
        

