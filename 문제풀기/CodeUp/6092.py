student_list = []

for i in range(24):
    student_list.append(0)

n = int(input())
a = input().split()


for i in range(n):
    student_list[int(a[i])] += 1

for i in range(1, 24):
    print(student_list[i], end=' ')