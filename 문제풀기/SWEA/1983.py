
import sys

sys.stdin = open("_1983.txt", "r")

T = int(input())

scores = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    students = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        students.append(a*0.35 + b*0.45 + c*0.2)

    student_K = students[K-1]
    students.sort(reverse=True)

    answer = students.index(student_K) // (N //10)
    print(f'#{test_case} {scores[answer]}')
    