R, C, K = map(int, input().split())

if K == 1:      # 어떤 크기든 1 번씩 방문은 할 수 있음.
    print(1)
elif R % 2 == 0 or C % 2 == 0: # 행 or 열이 2의 배수일 경우 K에 상관없이 성립.
    print(1)
else:
    print(0)
