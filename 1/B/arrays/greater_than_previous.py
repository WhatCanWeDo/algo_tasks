n = int(input())
lts = list(map(int, input().split()))
quantity = 0

for i in range(1, n):
    if lts[i - 1] < lts[i]:
        quantity += 1
print(quantity)
