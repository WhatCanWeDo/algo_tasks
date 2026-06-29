n = int(input())
matrix = []
road = 0

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range (n):
    for j in range (i+1, n):
        if matrix[i][j] == 1:
            road += 1 
print(road)
