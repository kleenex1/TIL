import sys

sys.stdin = open("_저항.txt")

T = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

a = input()
b = input()
c = input()

print("{}".format(int(str(T[a])+str(T[b]))*10**T[c]))