n_list = []

for i in range(9):
    i = int(input())
    n_list.append(i)

print(n_list)

index_max = n_list.index(max(n_list))

print(max(n_list), index_max + 1)
