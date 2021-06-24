from typing import List

def solution(islands: List[List[int]])->int :

    numOfIslands=0

    stack=[]

    row,col = len(islands), len(islands[0])

    # 시작점 찾기
    for i in range(len(islands)):
        if 1 in islands[i]:
            start= (i,islands[i].index(1))

    #동서남북 탐색
    def findOne(row, col):
        stack.append((row,col))
        islands[row][col]=0
        print(stack)
        #East
        if col<(len(islands[0])-1) and islands[row][col+1]==1:
            findOne(row,col+1)

        #West
        elif col>0 and islands[row][col-1]==1 :
            findOne(row,col-1)

        #South
        elif row<(len(islands)-1) and islands[row+1][col]==1:
            findOne(row+1,col)

        #North 
        elif row>0 and islands[row-1][col]==1:
            findOne(row-1,col)

        #Every Direction has zero
        else:
            stack.pop()
            if stack:
                prevRow, prevCol = stack.pop()
                findOne(prevRow,prevCol)

    

    def findIslands():
        nonlocal numOfIslands
         
        #find there is any other islands left
        for i in range(len(islands)):
            if 1 in islands[i]:
                numOfIslands+=1
                start= (i,islands[i].index(1))
                findOne(start[0],start[1])
              

        return numOfIslands
    


    return findIslands()

print(solution([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]))


            
