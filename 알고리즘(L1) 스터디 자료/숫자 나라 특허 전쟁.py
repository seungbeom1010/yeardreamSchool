def main():
    
    result = 0
    
    for i in range(1, int(input())):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    
    print(result)
    
if __name__ == "__main__":
    main()
