from typing import List

class Solution:
    def findSol(self, nums:List[int]):
        current=0
        left=0
        right=0

        # 시작부분 음수 제거
        for i in range(len(nums)):
            if(nums[i]<0):
                continue

            else:
                left=right= i
                break

        if(max(nums)<0):
            return max(nums)

        sum=nums[left]

        startIndex=left
        endIndex=len(nums)


        maxList=[sum,left,right]

        for i in range(startIndex+1,endIndex):
            current=nums[i]
            if(sum<=0 and current>=0):
                left=i
                right=i       
                sum=current
            elif(sum<=0 and current<=0):
                sum+=current
            elif(sum>=0 and current>=0):
                right=i
                sum+=current
            elif(sum>=0 and current<=0):
                sum+=current
            

            if(maxList[0]<sum):
                maxList=[sum,left,right]

            print(maxList)


        return maxList[0]


if __name__ =="__main__":
    sol = Solution()
    print(sol.findSol([1,2,-1,-2,2,1,-2,1,4,-5,4]))
