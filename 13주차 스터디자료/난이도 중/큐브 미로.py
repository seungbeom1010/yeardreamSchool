from collections import deque
# 작업 중
queue = deque()
n, m = list(map(int, input().split()))

adj = [[] for _ in range(n)]
for _ in range(m):
    src, dest = map(int, input().split())
    adj[src].append(dest)
    adj[dest].append(src)

