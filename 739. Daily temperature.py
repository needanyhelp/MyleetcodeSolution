from typing import List

def solution(T : List[int]):
    result=[0]*len(T)


    for i in range(len(T)-1):
        for j in range(i+1,len(T)):
            if T[i]<T[j]:
                result[i] = j-i
                break

    print(result)

solution([73, 74, 75, 71, 69, 72, 76, 73])
