import sys

sys.stdin = open("_행복한지.txt")

feeling = input()

happy = ":-)"
sad = ":-("

if feeling.count(happy) == 0 and feeling.count(sad) == 0:
    print("none")
elif feeling.count(happy) == feeling.count(sad):
    print("unsure")
elif feeling.count(happy) > feeling.count(sad):
    print("happy")
elif feeling.count(happy) < feeling.count(sad):
    print("sad")
