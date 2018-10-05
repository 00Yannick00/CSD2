#variables
import simpleaudio as sa
import time

samples = [sa.WaveObject.from_wave_file("/media/yannick/NieuwVolume/HKU/CSD_Rep/CSD2/python_basics/kick.wav")]
kickPlay = samples[0].play()

#show default BPM
bpm = 120
#write code to print BPM


#ask for BPM
print("Set bpm to?") 
bpm = float(input())
print(bpm)

#variables2
quarterNoteDuration = 60 / bpm
sixteenthNoteDuration = quarterNoteDuration / 4.0

#create list for timestamps
timestamps = []

#ask for rhytm, input[list] 
print("rhytm?") 
rhytm = [0]
duration = [float(x) for x in input().split()]

#voor elke input van ritme, voeg: 
for i in range (len(duration)):
  rhytm.append(float(duration[i]) * 4 + float(rhytm[i]))
print(rhytm)

# create a list to hold the timestamps
timestamps = []
for timestamp in rhytm:
  timestamps.append(timestamp * sixteenthNoteDuration)

# retrieve first timestamp
# NOTE: pop(0) returns and removes the element at index 0
timestamp = timestamps.pop(0)
# retrieve the startime: current time
startTime = time.time()
keepPlaying = True
# play the sequence
while keepPlaying:
  # retrieve current time
  currentTime = time.time()
  # check if the timestamp's time is passed
  if(currentTime - startTime >= timestamp):
    # play sample
    samples[0].play()

    # if there are timestamps left in the timestamps list
    if timestamps:
      # retrieve the next timestamp
      timestamp = timestamps.pop(0)
    else:
      # list is empty, stop loop
      keepPlaying = False
      time.sleep(0.001)





