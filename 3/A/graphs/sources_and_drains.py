n = int(input())

matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

sources = []  
drains = []    

for i in range(n):
    has_incoming = False
    for j in range(n):
        if matrix[j][i] == 1:
            has_incoming = True
            break
    if not has_incoming:
        sources.append(i + 1)  

    has_outgoing = False
    for j in range(n):
        if matrix[i][j] == 1:
            has_outgoing = True
            break
    if not has_outgoing:
        drains.append(i + 1)  

print(len(sources))  
for source in sources:
    print(source)

print(len(drains))  
for sink in drains:
    print(sink)
