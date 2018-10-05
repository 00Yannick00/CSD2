#variables
import simpleaudio as sa
import time
samples = [sa.WaveObject.from_wave_file("/media/yannick/NieuwVolume/HKU/CSD_Rep/CSD2/python_basics/audio_files/kick.wav")]


#show default BPM
bpm = 120
a = "current bpm: "
b = str(bpm)
print(a + b)
time.sleep(0.3)
print("keep current bpm? y/n")
c = input()
if c=="n":
  print("Set bpm to?") 
  bpm = float(input())
if not (c=="y" or "n"):
  bpm = 60
  print("you fool! you pressed the wrong button. your bpm is now 60.")   

#variables2

quarterNoteDuration = 60 / bpm
sixteenthNoteDuration = quarterNoteDuration / 4.0

#create list for timestamps
timestamps = []

#ask for rhytm, input[list] 
template = """input rhytm:\n\
notelegths:\n \
0.25 = 16th note\n \
0.5 = 8th note\n \
1 = quarternote\n \
etc."""
print(template)


#for every input in rhytm: 
#add element(float) to list, convert to the right note durations, 
#add to previous value to get timing of the 16th note, based on where the measure starts (0): 
rhytm = [0]
duration = [float(x) for x in input().split()]
for i in range (len(duration)):
  rhytm.append(float(duration[i]) * 4 + float(rhytm[i]))
print(rhytm)

# create a list with timestamps
timestamps = []
for timestamp in rhytm:
  timestamps.append(timestamp * sixteenthNoteDuration)

# NOTE: pop(0) returns and removes the element at index 0
timestamp = timestamps.pop(0)

# retrieve the startime: current time
startTime = time.time()
keepPlaying = True

# play the sequence
while keepPlaying:
  currentTime = time.time()
  if(currentTime - startTime >= timestamp):
    samples[0].play()
    # if there are timestamps left in the timestamps list
    if timestamps:
      # retrieve the next timestamp
      timestamp = timestamps.pop(0)
    else:
      # list is empty, stop loop
      keepPlaying = False
else:
      time.sleep(0.001)





