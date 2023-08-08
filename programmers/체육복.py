n = 4
lost = [2, 3]
reserve = [3, 4]

n = 5
lost = [2, 4, 5]
reserve = [2, 3, 5]

# 중복자원 --> 여벌이 있지만 도난당한 학생
# 중복자원 제거해주기
common_reserve = [i for i in lost if i in reserve]
for common in common_reserve:
    lost.remove(common)
    reserve.remove(common)

print(lost)
print(reserve)

# set로 크기별로 정렬해주기
s_lost = set(lost)
s_reserve = set(reserve)


for s in s_reserve:
    if s + 1 in s_lost:
        s_lost.remove(s+1)

    elif s - 1 in s_lost:
        s_lost.remove(s - 1)

print(n - len(s_lost))


"""
    while len(lost) and len(reserve) >= 1:
        if lost[a] - reserve[y] == 1 or -1:
            lost.remove(a) and reserve.remove(y)
            dog = len(lost)
        elif lost[a] - reserve[y] != 1 or -1:
            dog = len(lost) + 1

while 안되는 이유:
set not suscriptable
세트를 인덱스로 접근할 수가 없다

"""


"""
i = 0

def solution(n, lost, reserve):
    i = 0
    if len(lost) > len(reserve):
        while len(reserve) >= 1:
            if lost[i] - reserve[0] == 1 or -1:
                lost.pop(0)
                reserve.pop(i)    
            elif lost[i] - reserve[0] > 1:
                i +=1
    elif len(lost) <= len(reserve):
        while len(lost) >= 1:
            if lost[0] - reserve[i] == 1 or -1:
                lost.pop(0)
                
            elif lost[i] - reserve[0] > 1:
                i += 1
                
    return n - len(lost)
"""