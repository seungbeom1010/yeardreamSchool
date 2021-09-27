def main():
    
    request = int(input())
    
    peanut = 0
    chicken = 0
    protein = 0
    
    if (((request % 250) % 40) % 10) != 0:
        print(-1)
    
    if (((request % 250) % 40) % 10) == 0:
        
        if request > 250:
            protein += request // 250

        if request % 250 != 0:
            chicken += (request % 250) // 40

        if (request % 250) % 40 != 0:
            peanut += ((request % 250) % 40) // 10

        result = [peanut, chicken, protein]

        print(*result)
    

if __name__ == "__main__":
    main()
