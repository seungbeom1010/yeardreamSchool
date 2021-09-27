def main():
    
    data_n = int(input())
    
    data_sum = 0
    
    for i in range(data_n):
        
        data_sum += int(input())
        
    print(str(data_sum)[:10])
    
    
    
if __name__ == "__main__":
    main()
