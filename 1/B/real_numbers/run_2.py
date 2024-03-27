inp = list(map(float, input().split()))

if len(inp) == 1:
    ran_kilometers = inp[0]
    distance = int(input())
else:
    ran_kilometers, distance = inp

total_distance = ran_kilometers
days = 1
eps = 1e-6

while abs(distance - ran_kilometers) > eps:
    ran_kilometers += ran_kilometers * 0.7
    total_distance += ran_kilometers
    days += 1

print(days)
