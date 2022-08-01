elec = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]


a = elec.index(input())
b = elec.index(input())
c = elec.index(input())

print((f'{(a*10+b)*10**c}'))