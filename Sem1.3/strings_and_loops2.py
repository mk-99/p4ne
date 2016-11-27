#!/usr/local/bin/python3

def classify(i):
    if not (i % 2):
        return ">"
    elif not (i % 3):
        return "^"
    elif not (i % 5):
        return "&"
    else:
        return "?"

for i in range(1, 21):
    for j in range(1, 21):
        print("%s%4d" % (classify(i*j), i*j), end=" ")
    print("")
