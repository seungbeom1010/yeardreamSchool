def main():
    
    n = int(input())
    change = 10000 - n    # 받아야 하는 거스름돈
    result = 0    # 거스름돈의 지폐 개수
    m = 10000 
    
    while m > 0:    # 10000원부터 1원까지 사용된 지폐 계수 구하기
        result += change // m    # 거스름돈 지불에 사용된 m 가치의 지폐 개수 result변수에 저장
        change = change % m    # m 가치의 지폐로 거스름돈 지불 후 남은 금액 change변수에 저장
        m = m / 10
    
    print(int(result))

if __name__ == "__main__":
    main()
