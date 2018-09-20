import time
import winsound


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
    winsound.PlaySound ("kick", winsound.SND_FILENAME)
    time.sleep(tsleep)
    