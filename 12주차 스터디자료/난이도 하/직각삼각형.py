def square(x):
    return x * x

def main():
    
    Tri_List = []
    
    while True:     # 0 나오기 전 input값 모두 Tri_List에 append
        Tri = sorted(list(map(int, input().split())))
        if Tri == [0]:
            break
            
        Tri_List.append(Tri)
    
    for i in Tri_List:      # 피타고라스의 정리 사용
        if square(i[0]) + square(i[1]) == square(i[2]):
            print('rightangle')
        else:
            print('triangle')

if __name__ == '__main__':
    main()