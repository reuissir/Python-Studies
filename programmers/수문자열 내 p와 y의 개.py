s = "pPoooyY"

def solution(s):
    countp = 0
    county = 0
    for i in s:
        if i.lower() == 'p':
            countp += 1
        elif i.lower() == 'y':
            county += 1

    if countp == county:
        return True
    elif countp != county:
        return False
    
print(solution(s))