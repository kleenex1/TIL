google = {}

N = int(input())
for _ in range(N):
    person, status = map(str, input().split())
    google[person] = status

staff = []
for key in google:
    if google[key] == 'enter':
        staff.append(key)

for person in sorted(staff, reverse=True):
    print(person)
