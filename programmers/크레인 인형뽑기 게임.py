board = [0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]
moves = [1,5,3,5,1,2,1,4]

stack = []
answer = 0

def solution(moves, board):
    for move in moves:
        column = move - 1    
        for row in board:
            if row[column] == 0:
                continue       
            elif row[column] > 0:
                stack.append(row[column])
                row[column] = 0
                break            
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
                
    return answer

        