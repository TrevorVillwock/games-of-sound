from pyo import Server, Events, EventSeq, Sig
import json
from instruments import HiHat, Snare, Kick
import customtkinter as ctk
from functools import partial
from gui import set_bpm, set_main_volume, set_tuplet, set_sample_speed, toggle_delay, toggle_reverb

BPM = 124
PAD = 10

MAIN_BUTTON_WIDTH = 100
MAIN_BUTTON_HEIGHT = 100

# starts pyo server which will create all audio
s = Server().boot()
s.start()

# starts customtkinter window containing all GUI elements
root = ctk.CTk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))
root.title("Polyrhthmic Drum Machine")
root.attributes("-fullscreen", True)

with open("settings.json", 'r') as file:
    settings = json.load(file)

s.recordOptions(filename = f"./drum_machine_take{settings['take_number']}.wav")

settings['take_number'] = settings['take_number'] + 1
presets = settings["presets"]
print(presets["1"]["hihat1"]["tuplet"])

with open("settings.json", 'w') as file:
    json.dump(settings, file, indent=4)
            
hihat1 = Events(
    instr=HiHat,
    beat=1/presets["1"]["hihat1"]["tuplet"],
    amp=1,
    bpm=BPM,
    sample_speed=0.7,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

hihat2 = Events(
    instr=HiHat,
    beat=0.5,
    amp=EventSeq([1, 0, 1, 0, 1]),
    bpm=BPM,
    sample_speed=1.0,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

hihat3 = Events(
    instr=HiHat,
    beat=0.2,
    amp=EventSeq([1, 1, 1, 1, 1]),
    bpm=BPM,
    sample_speed=1.0,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()
 
snare = Events(
    instr=Snare,
    beat=0.5,
    amp=EventSeq([0, 0, 1, 0, 0, 0, 1, 0]), # amp = amplitude = volume
    bpm=BPM,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

kick = Events(
    instr=Kick,
    beat=0.5,
    amp=EventSeq([1, 0, 0, 0, 1, 0, 0, 0,
                  1, 0, 0, 0, 1, 0, 0, 1]),
    bpm=BPM,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

instruments = [hihat1, hihat2, hihat3, snare, kick]

main_control_bar = ctk.CTkFrame(root, width=1000, height=100)

play_button = ctk.CTkButton(main_control_bar, text="Play", width=MAIN_BUTTON_WIDTH, height=MAIN_BUTTON_HEIGHT, fg_color="green")
stop_button = ctk.CTkButton(main_control_bar, text="Stop", width=MAIN_BUTTON_WIDTH, height=MAIN_BUTTON_HEIGHT, fg_color="grey")
record_button = ctk.CTkButton(main_control_bar, text="Record", width=MAIN_BUTTON_WIDTH, height=MAIN_BUTTON_HEIGHT, fg_color="red")

bpm_label = ctk.CTkLabel(main_control_bar, text='BPM')
wrapped_set_bpm = partial(set_bpm, instruments=instruments)
bpm_slider = ctk.CTkSlider(main_control_bar, command=wrapped_set_bpm, from_=60, to=200)

main_volume_label = ctk.CTkLabel(main_control_bar, text='Volume')
wrapped_set_main_volume = partial(set_main_volume)
main_volume_slider = ctk.CTkSlider(main_control_bar, command=wrapped_set_main_volume, from_=60, to=200)

hihat1_delay_button = ctk.CTkButton(root, text="Delay", width=PAD, height=2, fg_color="black")
hihat1_delay_toggle = partial(toggle_delay, button=hihat1_delay_button, instrument=hihat1)
hihat1_delay_button.configure(command=hihat1_delay_toggle)

hihat1_reverb_button = ctk.CTkButton(root, text="Reverb", width=PAD, height=2, fg_color="black")
hihat1_reverb_toggle = partial(toggle_reverb, button=hihat1_reverb_button, instrument=hihat1)
hihat1_reverb_button.configure(command=hihat1_reverb_toggle)

hihat1_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuplet')
hihat1_set_tuplet = partial(set_tuplet, instrument=hihat1)
hihat1_tuplet_slider = ctk.CTkSlider(root, command=hihat1_set_tuplet, from_=1, to=12)

hihat1_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 1 tuning')
hihat1_set_sample_speed = partial(set_sample_speed, instrument=hihat1)
hihat1_tuning_slider = ctk.CTkSlider(root, command=hihat1_set_sample_speed, from_=0.1, to=2.0)

hihat2_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="black")
hihat2_delay_toggle = partial(toggle_delay, button=hihat2_delay_button, instrument=hihat2)
hihat2_delay_button.configure(command=hihat2_delay_toggle)

hihat2_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="black")
hihat2_reverb_toggle = partial(toggle_reverb, button=hihat2_reverb_button, instrument=hihat2)
hihat2_reverb_button.configure(command=hihat2_reverb_toggle)

hihat2_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuplet')
hihat2_set_tuplet = partial(set_tuplet, instrument=hihat2)
hihat2_tuplet_slider = ctk.CTkSlider(root, command=hihat2_set_tuplet, from_=1, to=12)
hihat2_tuplet_slider.configure(command=hihat2_set_tuplet)

hihat2_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuning')
hihat2_set_sample_speed = partial(set_sample_speed, instrument=hihat2)
hihat2_tuning_slider = ctk.CTkSlider(root, command=hihat2_set_sample_speed, from_=0.1, to=2.0)

hihat3_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="black")
hihat3_delay_toggle = partial(toggle_delay, button=hihat3_delay_button, instrument=hihat3)
hihat3_delay_button.configure(command=hihat3_delay_toggle)

hihat3_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="black")
hihat3_reverb_toggle = partial(toggle_reverb, button=hihat3_reverb_button, instrument=hihat3)
hihat3_reverb_button.configure(command=hihat3_reverb_toggle)

hihat3_tuplet_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuplet')
hihat3_set_tuplet = partial(set_tuplet, instrument=hihat3)
hihat3_tuplet_slider = ctk.CTkSlider(root, command=hihat3_set_tuplet, from_=1, to=12)
hihat3_tuplet_slider.configure(command=hihat3_set_tuplet)

hihat3_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuning')
hihat3_set_sample_speed = partial(set_sample_speed, instrument=hihat3)
hihat3_tuning_slider = ctk.CTkSlider(root, command=hihat3_set_sample_speed, from_=0.1, to=2.0)

root.columnconfigure(0, weight=1)
main_control_bar.grid(column=0, row=0, sticky="ew")

# distributes elements in main control bar
# for i in range(0, 12):
#     main_control_bar.columnconfigure(i, weight=1)

play_button.grid(column=0, row=0, columnspan=1, padx=5)
stop_button.grid(column=1, row=0, columnspan=1, padx=5)
record_button.grid(column=2, row=0, columnspan=1, padx=5)

bpm_label.grid(column=3, row=0, columnspan=1)
bpm_slider.grid(column=4, row=0, columnspan=5)

main_volume_label.grid(column=10, row=0, columnspan=1)
main_volume_slider.grid(column=11, row=0, columnspan=1)

# hihat1_delay_button.pack(pady=20)
# hihat1_reverb_button.pack(pady=20)
# hihat1_tuning_slider_label.pack(pady=PAD)
# hihat1_tuning_slider.pack(pady=PAD)
# hihat1_tuplet_slider_label.pack(pady=PAD)
# hihat1_tuplet_slider.pack(pady=PAD)

# hihat2_delay_button.pack(pady=20)
# hihat2_reverb_button.pack(pady=20)
# hihat2_tuning_slider_label.pack(pady=PAD)
# hihat2_tuning_slider.pack(pady=PAD)
# hihat2_tuplet_slider_label.pack(pady=PAD)
# hihat2_tuplet_slider.pack(pady=PAD)


# hihat3_delay_button.pack(pady=20)
# hihat3_reverb_button.pack(pady=20)
# hihat3_delay_button.pack(pady=20)
# hihat3_reverb_button.pack(pady=20)
# hihat3_tuplet_slider_label.pack(pady=PAD)
# hihat3_tuplet_slider.pack(pady=PAD)
# hihat3_tuning_slider.pack(pady=PAD)
# hihat3_tuning_slider_label.pack(pady=PAD)

root.mainloop()