#!/usr/local/bin/python3

def simple_compare(x):
    return x

def len_compare(x):
    return len(x)

def compare_2(x):
    return x[1]

def sort1(what_to_sort, compare_func=simple_compare):
    v = what_to_sort
    for i in range(0, len(v)):
        for j in range(i, len(v)):
            if compare_func(v[j]) < compare_func(v[i]):
                temp_variable = v[j] # swap v[i] with v[j]
                v[j] = v[i]
                v[i] = temp_variable
    return v


l = [10, 15, 111, 40, 80]
print(sorted(l))
l = ["One", "Two", "Three", "Four", "Five", "Six"]
print(sorted(l))
print(sorted(l, key=len_compare))
print(sorted(l, key=compare_2))
