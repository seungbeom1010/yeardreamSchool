def str_comp(n, i):
    
    if i == len(n) - 1: 
        return n[i]
    
    else:
        if n[i+1] == '(':
            return int(n[i]) * str_comp(n, i+2)
        else:
            return n[i] + str_comp(n, i+1)

def main():
    
    n = list(map(str, input().rstrip(')')))

    print(len(str_comp(n, 0)))

if __name__ == '__main__':
    main()

# 56(5318537442(20953049099(46087646(65950111(2))))

# print(len('5' + 6 * ('531853744' + 2 * ('2095304909' + 9 *('4608764' + (6 * ('6595011'+ (1*'2'))))))))