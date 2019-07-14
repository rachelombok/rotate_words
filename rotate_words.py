# Rachel Ombok
# CS UY 1114
# Homework 6
# 26 Oct 2018

def rotate(s):
    n = 0
    p = 1
    new_str = s[p:] + s[n:p]
    return new_str

def rotates(s, n):
    if n == 0:
        s = s
    while n > 0:
            s = rotate(s)
            n -= 1
    return s

def all_rotations(s):
    new_str = s
    for i in range(len(s)):
        new_str = rotates(s, i)
        print(new_str)
        






