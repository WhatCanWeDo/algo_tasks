n, skills = map(int, input().split())

tasks = []

for _ in range(n):
    a, b = map(int, input().split())
    tasks.append((a, b))

c = len(tasks)

for i in range(c - 1):
    for j in range(n - 1 - i):
        if tasks[j] > tasks[j + 1]:
            tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
            

solved_count = 0

for a, b in tasks:
    if skills >= a:
        solved_count += 1
        skills += b
    else:
        break
print(solved_count)
