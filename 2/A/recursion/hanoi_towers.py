def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish # Вспомогательный колышек
        move(n - 1, start, temp )
        print(n, start,  finish)
        move(n - 1, temp, finish)

move(int(input()), 1, 3)
