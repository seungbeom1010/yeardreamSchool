from sys import stdin

def shopping(products, n, s):

    count = []  # 최소금액이 맞춰질때, 상품의 개수
    for i in range(n): # 시작점
        clothes = 1
        sum_money = [] # 구간합을 저장하는 리스트, 시작점이 달라질 때마다 reset
        sum_money.append(products[i])
        if sum_money[-1] >= s:
            count.append(clothes)
        for j in range(i+1,n):
            t = sum_money[-1] + products[j]
            clothes += 1
            if t < s:
                sum_money.append(t)
            else:
                count.append(clothes)
                break

    if len(count) == 0:
        return 0
    return(min(count))


def main():
    n,s = map(int, input().split())  # n=상품의 개수, s = 쇼핑에 사용할 최소금액
    products = list(map(int, stdin.readline().split()))  # 상품리스트
    print(shopping(products, n, s))


if __name__ == "__main__":
    main()