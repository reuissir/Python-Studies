s = list(input())

for i in 'abcdefghijklmnopqrstuvwxyz':
    if i not in s:
        print(-1, end = ' ')
    else:
        print(s.index(i), end = ' ')