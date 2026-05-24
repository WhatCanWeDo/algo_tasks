data = [0] * 200

head = 100
tail = 100

while True:

    command = input().split()

    if command[0] == "push_front":
        head -= 1
        data[head] = command[1]
        print("ok")

    elif command[0] == "push_back":
        data[tail] = command[1]
        tail += 1
        print("ok")

    elif command[0] == "pop_front":
        if head == tail:
            print("error")
        else:
            print(data[head])
            head += 1

    elif command[0] == "pop_back":
        if head == tail:
            print("error")
        else:
            tail -= 1
            print(data[tail])

    elif command[0] == "front":
        if head == tail:
            print("error")
        else:
            print(data[head])

    elif command[0] == "back":
        if head == tail:
            print("error")
        else:
            print(data[tail - 1])

    elif command[0] == "size":
        print(tail - head)

    elif command[0] == "clear":
        head = 100
        tail = 100
    
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break
    