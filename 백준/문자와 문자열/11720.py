M = int(input())
a = list(map(int, input().strip()))

answer = 0
for i in a:
    answer += i
    
print(answer)
