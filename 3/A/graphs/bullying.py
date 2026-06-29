n = int(input())
matrix = []
min_length = float('inf')
best_route = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


for i in range(n):
    for j in range (i + 1, n):
        for k in range (j + 1, n):
            length = matrix[i][j] + matrix[j][k] + matrix[k][i]
            if length < min_length:
                min_length = length
                best_route = [i+1, j+1, k+1]

print(best_route)
