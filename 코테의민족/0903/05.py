words = input()
stack = []
ppap = ["P", "P", "A", "P"]
for i in range(len(words)):
    stack.append(words[i])
    if stack[-4:] == ppap:
        del stack[-4:]
        stack.append("P")

if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")