#!/usr/local/bin/python3

def fib(n):
    a, b = 1, 1

    step = 0
    while step < n:
        yield a
        b, a = a + b, b
        step += 1

def fibr(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibr(n - 1) + fibr(n - 2)

for i in range(50):
    print(fibr(i))

