# 인풋값을 전부 대문자로 바꾸기
a = input().upper()
seta = list(set(a))
lista = []

# 각 단어마다 개수 파악하기
for i in seta:
    lista.append(a.count(i))

# 최댓값이 1개보다 많으면 "?"을 출력    
if lista.count(max(lista)) > 1:
    print('?')
# 최댓값이 하나일 때 해당 알파벳을 출력해주기   
else:
    print(seta[lista.index(max(lista))])   
    