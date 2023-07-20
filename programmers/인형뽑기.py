board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 4, 1], [0, 0, 4, 1, 1], [1, 1, 1, 1, 1]]
bag = []
moves = [3, 2, 1, 4, 5]



def solution(board, moves):
    popped = 1
    
    for move in moves:
        # moves : 열
        # index - 1 필수
        column = move - 1
        # 행
        for row in range(len(board)):
            if board[row][column] == 0:
                continue
            elif board[row][column] > 0:
                bag.append(board[row][column])
                board[row][column] = 0
                    
                if len(bag) >= 2:
                    for element in bag:
                        if element == bag[-1]:
                            bag.remove(element)
                            bag.remove(bag[-1])
                            popped += 1 
                                    
                break
            
       
                   
    return popped

print("----solution(board, moves) ----")
print(solution(board, moves))
print("----board----")
print(board)
print("----bag----")
print(bag)
