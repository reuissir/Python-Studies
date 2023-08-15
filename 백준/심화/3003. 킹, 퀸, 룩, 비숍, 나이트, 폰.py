Found = list(map(int, input().split()))
Answer = [1, 1, 2, 2, 2, 8]

for i in range(len(Found)):
    print(Answer[i] - Found[i], end =' ')
