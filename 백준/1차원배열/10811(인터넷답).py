"""
인터넷에서 찾은 보다 직관적이고 간편한 답이다.
reverse()라는 함수를 이용했다는 점에서 풀이에 많은 복잡한 과정을 생략해줬다.
    """

M, N = map(int, input().split())

# 바구니 만들어주기
Basket = [a+1 for a in range(M)]
print(Basket)
    
for x in range(N):
    i, j = map(int, input().split())
    # 역순으로 바꿔줄 범위를 temp라는 변수에 저장해주고
    temp = Basket[i-1:j]
    print(temp)
    # 지정해준 범위 temp를 reverse()함수로 역순으로 변경해주기
    temp.reverse()
    # 최종적으로 Basket을 update해주기
    Basket[i-1:j] = temp
    print(Basket, " ' + temp' ")