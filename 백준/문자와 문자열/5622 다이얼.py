test = str(input().strip())

bag = []
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    0123456789
print(len(a))

for i in test:
    if a.index(i) <= 2:
        bag.append(3)
    elif a.index(i) <= 5:
        bag.append(4)
    elif a.index(i) <= 8:
        bag.append(5)
    elif a.index(i) <= 11:
        bag.append(6)
    elif a.index(i) <= 14:
        bag.append(7)
    elif a.index(i) <= 18:
        bag.append(8)
    elif a.index(i) <= 21:
        bag.append(9)
    elif a.index(i) <= 25:
        bag.append(10)
    
print(sum(bag))


print(test, "test")
print(test[0], "test[0]")
print("------------------")