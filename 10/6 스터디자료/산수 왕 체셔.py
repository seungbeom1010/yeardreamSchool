A, B, C = map(int, input().split())

def exp(A, B, C):
    if B == 1: # 1번만 곱하는 경우
        return A % C 
    elif B % 2 == 0: # B가 짝수인 경우
        x = exp(A, B/2, C)
        return (x * x) % C
    else: # 홀수의 경우
        y = exp(A, (B-1)/2, C)
        return (y * y * A) % C  

print(exp(A, B, C))
