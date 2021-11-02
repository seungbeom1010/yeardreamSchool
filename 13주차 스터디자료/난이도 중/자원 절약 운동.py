from sys import stdin
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = []
    
    res = [0] * len(graph)
    
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                res[i] = res[p] + 1
    
    return sum(res)

def main():
    n, m = map(int, stdin.readline().split())
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        node, adj = map(int, stdin.readline().split())
        graph[node].append(adj)
        graph[adj].append(node)
    
    result = []
    
    for i in range(1, n + 1):
        result.append(bfs(graph, i))
    
    print(result.index(min(result)) + 1)

if __name__ == '__main__':
    main()