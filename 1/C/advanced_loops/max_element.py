n = int(input())
elements = (int(s) for s in input().split())
max_ = -100

for i in elements:
    if i > max_:
        max_ = i

print(max_)
