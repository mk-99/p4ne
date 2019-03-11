#!/usr/local/bin/python3

def classify(i):
    if not (i % 2):
        return "43"
    elif not (i % 3):
        return "45"
    elif not (i % 5):
        return "46"
    else:
        return "42"


for i in range(1, 21):
    for j in range(1, 21):
        print("\x1b[%sm%4d\x1b[39m" % (classify(i * j), i * j), end="")
    print("")
