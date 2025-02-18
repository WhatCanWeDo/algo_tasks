n, m, k = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

pref = []
for _ in range(n + 1):
    row = []
    for d in range(m + 1):
        row.append(0)
    pref.append(row)


for i in range(1, n + 1):
    for j in range(1, m + 1):
        pref[i][j] = matrix[i - 1][j - 1] + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    s = pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1]
    print(s)
