n = 5
lost = [2, 4]
reserve = [1, 3, 5]


def solution(n, lost, reserve):
    i = 0

    if len(lost) < len(reserve): 
        while len(lost) >= 1:
            if reserve[i] - lost[i] == 1 or -1:
                lost.pop(i)
                reserve.append(i)
            elif len(lost) == 0:
                break
        return len(reserve)
        
    else: 
        return n - len(lost) + len(reserve)