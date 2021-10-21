
len_n = int(input())
n_list = [int(x) for x in input().split()]
n_change = int(input())
int_n_list = list(map(int, n_list))

while n_list[-1] != min(n_list) or n_change != 0:
        max_num = max(int_n_list[:n_change+1])
        n_list.insert(0, max_num)
        del n_list[int_n_list.index(max_num)]
        n_change = n_change - int_n_list.index(max_num)
        


print("".join(n_list))