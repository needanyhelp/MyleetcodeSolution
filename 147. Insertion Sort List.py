from typing import List


def solution(arraylist: List[List[int]]):
    result=[]
    for i in range(len(arraylist)-1):
        for j in range(i+1, len(arraylist)):
            if not(arraylist[i][1]<arraylist[j][0] or arraylist[i][0]>arraylist[j][1]):
                temp=arraylist[i]+arraylist[j]
                temp_min=min(temp)
                temp_max=max(temp)
                temp=[temp_min,temp_max]

                arraylist[i]=temp
                arraylist[j]=[0,0]

    result=set(map(tuple,([x if x!=[0,0] else[0,0] for x in arraylist])))
    result.remove((0,0))

    
    return result

        
        
    
a=solution([[1,3],[2,6],[8,10],[15,18]])
print(a)
b=solution([[1,3],[0,0],[0,0]])
print(b)

