stack = []

while True:
    command = input().split()

    if command[0] == "push":
        number = int(command[1])
        stack.append(number)
        print("ok")
    elif command[0] == "pop":
        value = stack.pop()
        print(value)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "back":
        print(stack[-1])
    elif command[0] == "clear":
        stack.clear()
        print("ok")
    elif command[0] == "exit":
        print("bye")
        break