first_number = int(input())
second_number = int(input())
third_number = int(input())
mx = first_number

if second_number > mx:
    mx = second_number
if third_number > mx:
    mx =  third_number

print(mx)
