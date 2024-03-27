number_students = int(input())
student_growth = [int(s) for s in input().split()]
p_height = int(input())
count = len(student_growth) + 1

for i in range(len(student_growth)):
    if p_height > student_growth[i]:
        count = i + 1
        break

print(count)
