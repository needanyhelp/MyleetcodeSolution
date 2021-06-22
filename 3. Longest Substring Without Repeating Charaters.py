from typing import DefaultDict


def twoPointer(s: str)->int : 

    strDict=DefaultDict(int)
    maxVal=0
    left=right=0

    for idx,char in enumerate(s):
        #char가 존재하는 경우 left포인터 이동
        if char in strDict:
            left=strDict[char]+1
            strDict[char]=idx
        else:
            
            strDict[char]=idx

        right=idx

        maxVal=max(maxVal,right-left+1)
    
    return maxVal

        
print(twoPointer('pwwkew'))
