n = input()

if len(n) == 2:
    print(int(n[0])+int(n[1]))
elif int(n[-2:]) == 10:
    print(int(n[:-2]) + 10)
else:
    print(int(n[:-1]) + int(n[-1]))

# commit변경