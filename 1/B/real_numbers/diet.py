X, Y, Z = map(float, input().split())
N = int(input())
total_protein = 0
total_fat = 0
total_carbohydrate = 0
eps = 1e-6

for i in range(N):
    Ai, Bi, Ci, Qi = map(float, input().split())
    total_protein += Ai * Qi
    total_fat += Bi * Qi
    total_carbohydrate += Ci * Qi

if total_protein + eps >= X and total_fat + eps >= Y and total_carbohydrate + eps >= Z:
    print("YES")
else:
    print("NO")
