from sys import stdin

l, r, c = map(int, stdin.readline().split())

cube = []

for i in range(c):
    maze = []
    for j in range(r + 1):
        m = list(map(str, stdin.readline().split()))
        if not m:
            continue
        elif '0' in m:
            break
        else:
            maze.append(m)
    cube.append(maze)

