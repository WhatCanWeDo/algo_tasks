n = int(input())
nums = list(map(int, input().split()))
max_ = nums[0]
a = 1

for i in range(1, n):
    if nums[i] > max_:
        max_ = nums[i]
        a = i + 1

print(a)
