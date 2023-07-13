# number of elements in list
n = int(input())

# create list
n_list = list(map(int, input().split()))

v = int(input("Type in number you're looking for: "))

print(n_list.count(v))


""" c = input("Type in numbers to insert into list: ")
n_list = c.split()
print(n_list)
"""

""" 
count = 0
for i in list:
    if i == v:
        count += 1

if count == 0:
    print(0)
elif count >= 1:
    print(count)
    """
