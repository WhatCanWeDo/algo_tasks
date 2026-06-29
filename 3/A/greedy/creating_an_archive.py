memory, users = map(int, input().split())
memory_users = []
counter = 0
total = 0
for _ in range(users):
    memory_users.append(int(input()))

memory_users.sort()

for i in memory_users:
    if total + i <= memory:
        total += i
        counter += 1
    else:
        break

print(counter)
