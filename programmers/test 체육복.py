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
