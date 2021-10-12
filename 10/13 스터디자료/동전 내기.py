def main():

    coin_array = list(input()) # ['0', '0', '0', '1', '1', '0', '0']

    result = [0, 0] # [앞면을 뒤집을 경우, 뒷면을 뒤집는 경우]

    result[int(coin_array[0])] = 1 # 문자열 시작하는 면 + 1

    for i in range(len(coin_array)-1):
        if coin_array[i] == coin_array[i+1]: # 다음 문자열 인덱스와 같은 면일 경우 pass
            pass
        else:
            result[int(coin_array[i+1])] += 1 # 다음 문자열 인덱스와 다른 면일 경우, 다른 면 + 1

    print(min(result)) # 최솟값 출력

if __name__ == "__main__":
    main()
