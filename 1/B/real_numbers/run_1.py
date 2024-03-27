ran_kilometers, distance = map(float, input().split())
days = 1
eps = 1e-6

while abs(distance - ran_kilometers) > eps:
    ran_kilometers += ran_kilometers * 0.7
    days += 1
    
print(days)
