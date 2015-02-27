#!/usr/bin/env python
import itertools


def xxds(string):
    return ''.join(list(map(lambda ch: hex(ord(ch)[2:]), string)))

def xxdb(byt):
    return ''.join(list(map(lambda b: hex(b)[2:], byt)))

def xxdgen(data, func):
    for byte in data:
        yield hex(func(data))[2:]

def xxdf(filename):
    with open(filename, 'rb') as infile:
        for line in infile:
            oline = xxdb(line)
            print(oline, end="")

def xxd(data):
    if isinstance(data, bytes):
        return xxdb(data)
    elif isinstance(data, str):
        return xxds(data)
    elif isinstance(data, file):
        return xxdf(data)

if __name__ == "__main__":
    import sys
    xxdf(sys.argv[1])
