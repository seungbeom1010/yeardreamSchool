def main():

    bottle = []
    cover = []
    
    for i in range(3):
        bottle.append(int(input()))
        
    for i in range(2):
        cover.append(int(input()))
    
    min_bottle = min(bottle)
    min_cover = min(cover)
    
    print(min_bottle + min_cover+10)

if __name__ == "__main__":
    main()
