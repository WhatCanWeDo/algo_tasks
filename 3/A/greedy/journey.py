#n - расстояние между пунктами, k - литров в баке 
n, k = map(int, input().split())

data = list(map(int, input().split()))
s = data[0]

fuel = k
pos = 0
ans = 0 

for i in range(1, s + 1):
    station = data[i]
    dist = station - pos
    if dist > k:
        print(-1)
        exit()
    if dist > fuel:
        ans += 1 
        fuel = k
    fuel -= dist
    pos = station

dist = n - pos
if dist > k:
    print(-1)
    exit()
if dist > fuel:
    ans += 1 

print(ans)