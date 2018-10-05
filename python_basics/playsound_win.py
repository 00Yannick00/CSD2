import time
import simpleaudio as sa
samples = [sa.WaveObject.from_wave_file("/media/yannick/NieuwVolume/HKU/CSD_Rep/CSD2/python_basics/kick.wav")]
kickPlay = samples[0].play()


print("hello, how many KICKS would you like?")
numPbtimes = int(input())

print("BPM?")
bpm = float(60/float(input()))


print("ritme??:")
lijst = [float(x) for x in range(numPbtimes)]
ritme = []
length = len(lijst)

for f in range(length):
    data=float(input())
    ritme.append(data)

for value in ritme:
    tsleep = float(float(value) *float(bpm))
    kickPlay
    time.sleep(tsleep)
    