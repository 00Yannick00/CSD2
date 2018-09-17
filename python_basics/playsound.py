print("hello, how many KICKS would you like?")
x = int(input())
for i in range(x):
    import os
    os.system("aplay /media/yannick/NieuwVolume/HKU/CSD_Rep/CSD2/python_basics/kick.wav")
    import time
    time.sleep(0.5)



