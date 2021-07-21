def solution(nums, target):
    resultIndex=0
    
    def searchBinary(newNums,target):
        nonlocal resultIndex

        if len(newNums)==1 and target==newNums[0]:
            resultIndex+=1
            return         

        midIndex=len(newNums)//2
        mid=newNums[midIndex]


        if target==mid:
            resultIndex+=midIndex+1
            return 
        elif target>mid:
            resultIndex+=midIndex+1
            return searchBinary(newNums[midIndex+1:], target)
            
        else:
            return searchBinary(newNums[:midIndex], target)
    
    searchBinary(nums,target)
    print(resultIndex-1)
    




solution([-1,0,3,5,9,12,13,14,15], 5)