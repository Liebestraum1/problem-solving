def solution(arr1, arr2):
    answer = []
    for a in arr1:
        row = []
        for b in zip(*arr2):
            result = 0
            for i in range(len(a)):
                result += a[i] * b[i]
            row.append(result)
        answer.append(row)
    
    return answer