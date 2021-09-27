def task_record(days, numbers):
    
    result = []
    sum = 0
    
    for i in range(days):
        value = numbers[i] * (i+1) - sum
        sum += value
        result.append(value)
    
    return result

def main():
    
    days = int(input())
    numbers = [int(x) for x in input().split()]
    
    print(*task_record(days, numbers))

if __name__ == "__main__":
    main()
