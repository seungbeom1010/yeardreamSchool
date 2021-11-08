from sys import stdin

def escape_cube():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

def main():
    l, r, c = map(int, stdin.readline().split())

    cube = []
    start = []
    end = []

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
                if m.find('S') != -1 and not start:
                    start = [m.find('S'), j, i]
                elif m.find('E') != -1 and not end:
                    end = [m.find('E', j, i)]
        cube.append(maze)


    
if __name__ == '__main__':
    main()