arr1 = [[1],[2]]
arr2 = [[3],[4]]

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for y in range(len(arr1[i])):
            arr1[i][y] += arr2[i][y]
            
    return arr1

print(arr1)
print(solution(arr1, arr2))