n = int(input())
matrix = []
bad_bridges = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

input()
colors = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] == 1:
            if colors[i] != colors[j]:
                bad_bridges += 1

print(bad_bridges)
