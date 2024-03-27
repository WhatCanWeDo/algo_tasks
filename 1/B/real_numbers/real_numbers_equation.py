sum_ = float(input())
sum_ += float(input())
amount = float(input())
amount = amount - sum_
eps = 1e-6

if abs(amount) < eps:
    print("YES")
else:
    print("NO")
