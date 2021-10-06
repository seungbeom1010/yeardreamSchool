N = int(input())

n_divisor = 1 # 약수 개수
n_stage = 1 # 스테이지 넘버


while n_divisor < N+1: # 희망 경품 개수와 약수 개수가 같아지기 전까지 반복
    divisor = [] # 약수 List
    ST = int(n_stage * (n_stage+1) / 2) #해당 스테이지 합산 점수

    for i in range(1, ST+1): #합산 점수 약수 구하기
        if ST % i == 0:
            divisor.append(i)
            
    n_divisor = len(divisor)
    n_stage += 1 

print(ST)
