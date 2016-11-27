#!/usr/local/bin/python3

i = 1

def classify(i):
    if not (i % 2):
        return ">"
    elif not (i % 3):
        return "^"
    elif not (i % 5):
        return "&"
    else:
        return "?"

while i <= 20:
    j = 1
    while j <= 20:
        print("%s%4d" % (classify(i*j), i*j), end=" ")
        j += 1
    print("")
    i += 1
