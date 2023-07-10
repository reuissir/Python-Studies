arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]


def solution(arr1, arr2):
    
    for i in range(len(arr1)):
        for y in range(len(arr1[i])):
            result = arr1[i][y] =+ arr2[i][y]
            
        return result

print(solution(arr1, arr2))