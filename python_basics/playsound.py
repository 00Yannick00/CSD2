import time
import os


print("hello, how many KICKS would you like?")
numPbtimes = int(input())

print("BPM?")
bpm = float(60/float(input()))
print(bpm)

print("ritme??:")
lijst = [float(x) for x in range(numPbtimes)]
ritme = []
length = len(lijst)

for f in range(length):
    data=float(input())
    ritme.append(data)

for value in ritme:
    tsleep = float(float(value) *float(bpm))
    os.system("aplay /media/yannick/NieuwVolume/HKU/CSD_Rep/CSD2/python_basics/kick.wav")
    time.sleep(tsleep)
    
    





