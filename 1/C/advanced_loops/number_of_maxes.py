nums = -1
max_ = 0
n_max = 0

while nums != 0:
    nums = int(input())
    if nums > max_:
        max_ = nums
        n_max = 1
    elif nums == max_:
        n_max += 1

print(n_max)
