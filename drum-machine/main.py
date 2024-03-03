from pyo import Server, Events, EventSeq, Sig
import json
from instruments import HiHat, Snare, Kick
import customtkinter as ctk
from functools import partial
from gui import set_bpm, set_main_volume, set_subdivision, set_sample_speed, toggle_delay, toggle_reverb

PAD = 10
MAIN_BUTTON_WIDTH = 100
MAIN_BUTTON_HEIGHT = 100
SEQUENCER_BUTTON_HEIGHT = 100

bpm = 124

hihat1_sequencer_button_width = 100
hihat2_sequencer_button_width = 100
hihat3_sequencer_button_width = 100
snare_sequencer_button_width = 100
kick_sequencer_button_width = 100

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
print(presets["1"]["hihat1"]["subdivision"])

with open("settings.json", 'w') as file:
    json.dump(settings, file, indent=4)
            
hihat1 = Events(
    instr=HiHat,
    beat=1/presets["1"]["hihat1"]["subdivision"],
    amp=1,
    bpm=bpm,
    sample_speed=0.7,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

hihat2 = Events(
    instr=HiHat,
    beat=0.5,
    amp=EventSeq([1, 0, 1, 0, 1]),
    bpm=bpm,
    sample_speed=1.0,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

hihat3 = Events(
    instr=HiHat,
    beat=0.2,
    amp=EventSeq([1, 1, 1, 1, 1]),
    bpm=bpm,
    sample_speed=1.0,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()
 
snare = Events(
    instr=Snare,
    beat=0.5,
    amp=EventSeq([0, 0, 1, 0, 0, 0, 1, 0]), # amp = amplitude = volume
    bpm=bpm,
    delay_is_on=Sig(0),
    reverb_is_on=Sig(0)
).play()

kick = Events(
    instr=Kick,
    beat=0.5,
    amp=EventSeq([1, 0, 0, 0, 1, 0, 0, 0,
                  1, 0, 0, 0, 1, 0, 0, 1]),
    bpm=bpm,
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

hihat1_frame = ctk.CTkFrame(root, width=1000, height=100)
hihat1_label = ctk.CTkLabel(hihat1_frame, text="Hihat 1", padx=10)

hihat2_frame = ctk.CTkFrame(root, width=1000, height=100)
hihat2_label = ctk.CTkLabel(hihat2_frame, text="Hihat 2", padx=10)

hihat3_frame = ctk.CTkFrame(root, width=1000, height=100)
hihat3_label = ctk.CTkLabel(hihat3_frame, text="Hihat 3", padx=10)

snare_frame = ctk.CTkFrame(root, width=1000, height=100)
snare_label = ctk.CTkLabel(snare_frame, text="Snare", padx=10)

kick_frame = ctk.CTkFrame(root, width=1000, height=100)
kick_label = ctk.CTkLabel(kick_frame, text="Kick", padx=10)

# the steps of the sequencer are buttons 
# so that they can be clicked to turn them on and off
hihat1_sequencer = []
hihat2_sequencer = []
hihat3_sequencer = []
snare_sequencer = []
kick_sequencer = []

for i in range(0, 16):
    hihat1_sequencer.append(ctk.CTkButton(hihat1_frame, text="0.5", width=hihat1_sequencer_button_width, height=SEQUENCER_BUTTON_HEIGHT))
    hihat2_sequencer.append(ctk.CTkButton(hihat2_frame, text="0.5", width=hihat2_sequencer_button_width, height=SEQUENCER_BUTTON_HEIGHT))
    hihat3_sequencer.append(ctk.CTkButton(hihat3_frame, text="0.5", width=hihat3_sequencer_button_width, height=SEQUENCER_BUTTON_HEIGHT))
    snare_sequencer.append(ctk.CTkButton(snare_frame, text="0.5", width=snare_sequencer_button_width, height=SEQUENCER_BUTTON_HEIGHT))
    kick_sequencer.append(ctk.CTkButton(kick_frame, text="0.5", width=kick_sequencer_button_width, height=SEQUENCER_BUTTON_HEIGHT))

all_sequencers = [hihat1_sequencer, hihat2_sequencer, hihat3_sequencer, snare_sequencer, kick_sequencer]

hihat1_delay_button = ctk.CTkButton(hihat1_frame, text="Delay", width=PAD, height=2, fg_color="black")
hihat1_delay_toggle = partial(toggle_delay, button=hihat1_delay_button, instrument=hihat1)
hihat1_delay_button.configure(command=hihat1_delay_toggle)

hihat1_reverb_button = ctk.CTkButton(hihat1_frame, text="Reverb", width=PAD, height=2, fg_color="black")
hihat1_reverb_toggle = partial(toggle_reverb, button=hihat1_reverb_button, instrument=hihat1)
hihat1_reverb_button.configure(command=hihat1_reverb_toggle)

hihat1_subdivision_slider_label = ctk.CTkLabel(hihat1_frame, text='Subdivision')
hihat1_set_subdivision = partial(set_subdivision, instrument=hihat1)
hihat1_subdivision_slider = ctk.CTkSlider(hihat1_frame, command=hihat1_set_subdivision, from_=1, to=12)

hihat1_tuning_slider_label = ctk.CTkLabel(hihat1_frame, text='Tuning')
hihat1_set_sample_speed = partial(set_sample_speed, instrument=hihat1)
hihat1_tuning_slider = ctk.CTkSlider(hihat1_frame, command=hihat1_set_sample_speed, from_=0.1, to=2.0)

hihat2_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="black")
hihat2_delay_toggle = partial(toggle_delay, button=hihat2_delay_button, instrument=hihat2)
hihat2_delay_button.configure(command=hihat2_delay_toggle)

hihat2_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="black")
hihat2_reverb_toggle = partial(toggle_reverb, button=hihat2_reverb_button, instrument=hihat2)
hihat2_reverb_button.configure(command=hihat2_reverb_toggle)

hihat2_subdivision_slider_label = ctk.CTkLabel(root, text='HiHat 2 subdivision')
hihat2_set_subdivision = partial(set_subdivision, instrument=hihat2)
hihat2_subdivision_slider = ctk.CTkSlider(root, command=hihat2_set_subdivision, from_=1, to=12)
hihat2_subdivision_slider.configure(command=hihat2_set_subdivision)

hihat2_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 2 tuning')
hihat2_set_sample_speed = partial(set_sample_speed, instrument=hihat2)
hihat2_tuning_slider = ctk.CTkSlider(root, command=hihat2_set_sample_speed, from_=0.1, to=2.0)

hihat3_delay_button = ctk.CTkButton(root, text="Delay", width=10, height=2, fg_color="black")
hihat3_delay_toggle = partial(toggle_delay, button=hihat3_delay_button, instrument=hihat3)
hihat3_delay_button.configure(command=hihat3_delay_toggle)

hihat3_reverb_button = ctk.CTkButton(root, text="Reverb", width=10, height=2, fg_color="black")
hihat3_reverb_toggle = partial(toggle_reverb, button=hihat3_reverb_button, instrument=hihat3)
hihat3_reverb_button.configure(command=hihat3_reverb_toggle)

hihat3_subdivision_slider_label = ctk.CTkLabel(root, text='HiHat 3 subdivision')
hihat3_set_subdivision = partial(set_subdivision, instrument=hihat3)
hihat3_subdivision_slider = ctk.CTkSlider(root, command=hihat3_set_subdivision, from_=1, to=12)
hihat3_subdivision_slider.configure(command=hihat3_set_subdivision)

hihat3_tuning_slider_label = ctk.CTkLabel(root, text='HiHat 3 tuning')
hihat3_set_sample_speed = partial(set_sample_speed, instrument=hihat3)
hihat3_tuning_slider = ctk.CTkSlider(root, command=hihat3_set_sample_speed, from_=0.1, to=2.0)

# root.columnconfigure(0, weight=1)

# distributes elements in main control bar
# for i in range(0, 12):
#     main_control_bar.columnconfigure(i, weight=1)

# Unsuccessful GPT-4 distribution:

# for i in range(14):  # Adjusted for extra columns for spacing
#     main_control_bar.columnconfigure(i, weight=1)

# Adjust grid placements with added padding columns
# play_button.grid(column=1, row=0, padx=5)  # Start from column 1 instead of 0
# stop_button.grid(column=2, row=0, padx=5)
# record_button.grid(column=3, row=0, padx=5)
# bpm_label.grid(column=4, row=0)
# bpm_slider.grid(column=5, row=0, columnspan=5)
# main_volume_label.grid(column=11, row=0)
# main_volume_slider.grid(column=12, row=0)

main_control_bar.grid(column=0, row=0, sticky="ew")
play_button.grid(column=0, row=0, columnspan=1, padx=5)
stop_button.grid(column=1, row=0, columnspan=1, padx=5)
record_button.grid(column=2, row=0, columnspan=1, padx=5)

bpm_label.grid(column=3, row=0, columnspan=1)
bpm_slider.grid(column=4, row=0, columnspan=5)

main_volume_label.grid(column=10, row=0, columnspan=1)
main_volume_slider.grid(column=11, row=0, columnspan=1)

hihat1_frame.grid(row=1, column=0, sticky="w")
hihat1_label.grid(row=1, column=0, sticky="w")
hihat1_subdivision_slider_label.grid(row=1, column=1)
hihat1_subdivision_slider.grid(row=1, column=2)
hihat1_tuning_slider_label.grid(row=1, column=3)
hihat1_tuning_slider.grid(row=1, column=4)
hihat1_delay_button.grid(row=1, column=5)
hihat1_reverb_button.grid(row=1, column=6)

for i in range(0, 5):
    for j in range(0, 16):
        all_sequencers[i][j].grid(row=i, column=j)

root.mainloop()

# hihat1_delay_button.pack(pady=20)
# hihat1_reverb_button.pack(pady=20)
# hihat1_tuning_slider_label.pack(pady=PAD)
# hihat1_tuning_slider.pack(pady=PAD)
# hihat1_subdivision_slider_label.pack(pady=PAD)
# hihat1_subdivision_slider.pack(pady=PAD)

# hihat2_delay_button.pack(pady=20)
# hihat2_reverb_button.pack(pady=20)
# hihat2_tuning_slider_label.pack(pady=PAD)
# hihat2_tuning_slider.pack(pady=PAD)
# hihat2_subdivision_slider_label.pack(pady=PAD)
# hihat2_subdivision_slider.pack(pady=PAD)

# hihat3_delay_button.pack(pady=20)
# hihat3_reverb_button.pack(pady=20)
# hihat3_delay_button.pack(pady=20)
# hihat3_reverb_button.pack(pady=20)
# hihat3_subdivision_slider_label.pack(pady=PAD)
# hihat3_subdivision_slider.pack(pady=PAD)
# hihat3_tuning_slider.pack(pady=PAD)
# hihat3_tuning_slider_label.pack(pady=PAD)