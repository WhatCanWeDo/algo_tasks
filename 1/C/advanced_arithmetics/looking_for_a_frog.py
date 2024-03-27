long, time = map(int, input().split())
n = time % (2 * long)
if n > long:
    n = 2 * long - n

print(n)
