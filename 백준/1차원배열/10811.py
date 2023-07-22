"""
문제
도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다. 

도현이는 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다. 도현이는 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고, 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.

바구니의 순서를 어떻게 바꿀지 주어졌을 때, M번 바구니의 순서를 역순으로 만든 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)

도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.

출력
모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

"""

"""
1~N 까지 총 N개의 바구니가 있고
바구니의 순서를 M번 바꾼다

"""


# N: 총 바구니 개수
# M: 역순으로 만들 바구니
N, M = map(int, input().split())
LIST = []

for a in range(N):
    LIST.append(a+1)
    
for m in range(M):
    i, j = map(int, input().split())
    if j - i == 1:
        LIST[i-1], LIST[j-1] = LIST[j-1], LIST[i-1]
        print(LIST, m)
    elif j - i > 1:        
        for y in range((round((j - i + 1) / 2))):
            LIST[i-1 + y], LIST[j-1-y] = LIST[j-1-y], LIST[i-1+y]
            print(LIST, y)
        
for i in LIST:
    print(i, end = " ")



"""
인터넷에서 찾은 훨씬 간단한 답

N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for i in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1 : j]
    temp.reverse()
    basketb[i-1:j] = temp
    
for i in range(N):
    print(basket[i], end = ' ')
    
    """
    
"""
# 재미삼아 실험해보기
# 리스트 중점으로 좌우 바꿔보기
test = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]


for i in range(len(test) // 2):
    test[i], test[-1 - i] = test[-1 - i], test[i]
    
print(test)

출력: [[9, 10], [7, 8], [5, 6], [3, 4], [1, 2]]
"""