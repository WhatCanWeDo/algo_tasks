data = [0] * 4
head = 0
tail = 0
count = 0 

def resize():
    global data, head, tail, count
    new_data = [0] * (len(data) * 2)

    for i in range(count):
        new_data[i] = data[(head + i) % len(data)]
        
    data = new_data
    head = 0
    tail = count

while True:
    command = input().split()

    if command[0] == "push":
        number = int(command[1])
        
        if count == len(data):
            resize()

        data[tail] = number
        tail = (tail + 1 ) % len(data)
        count += 1      
        print("ok")

    elif command[0] == "pop":
        if count == 0:
            print("error")
        else:
            print(data[head])
            head = (head + 1 ) % len(data)
            count -= 1 

    elif command[0] == "size":
        print(count)

    elif command[0] == "front":
        if count == 0 :
            print("error")
        else:
            print(data[head])

    elif command[0] == "clear":
        data = [0] * 4
        head = 0
        tail = 0 
        count = 0 
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break
    