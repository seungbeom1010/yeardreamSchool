node, leaf = map(int, input().split())

for i in range(node-1):
    if node - leaf > i:
        print(i, i+1)
    else:
        print(0, i+1)