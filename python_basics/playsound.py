print("hello, how many KICKS would you like?")

x = int(input())
for i in range(x):
    import winsound
    winsound.PlaySound ("kick", winsound.SND_FILENAME)
    import time
    time.sleep(0.5)
