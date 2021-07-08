import collections

def solution(n, t, m, timeTable:collections.deque):
    
    def timeConvert(minutes):
        div,mod=divmod(minutes,60)
        div=str(div)
        mod=str(mod)
        if len(div)<2:
            div='0'+div
        if len(mod)<2:
            mod='0'+mod

        return div+':'+mod
    
    
    
    #convert 09:00 to minutes
    busTime=9*60

    myArrivingTime=0

    timeTable=sorted(timeTable)

    for i,time in enumerate(timeTable):
        temp=list(map(int,time.split(':')))
        hour=60*temp[0]
        timeTable[i]=hour+temp[1]
    
    
    timeTable=collections.deque(timeTable)

    lastTime=9*60+(n-1)*t

    timeTable.append(lastTime)
    timeTable=sorted(timeTable)
    lastTimeIndex=timeTable.index(lastTime)
    timeTable=timeTable[:lastTimeIndex]
    

    timeTable=collections.deque(timeTable)

    if not timeTable:
        myArrivingTime=540+(n-1)*t
        return timeConvert(myArrivingTime)

    for i in range(n):
        for j in range(m):

            # if there is not enough sits
            if i==n-1 and len(timeTable)>=m:
                myArrivingTime=timeTable[m-1]-1
                break

            # if there is enough sits
            elif i==n-1 and len(timeTable)<m:
                myArrivingTime=timeTable[-1]
                if myArrivingTime < 540:
                    myArrivingTime=540
                break

            if timeTable[0]<=busTime:
                timeTable.popleft()

    



        busTime+=t

    return timeConvert(myArrivingTime)


print(solution(1,1,5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2, ["09:10", "09:09", "08:00"]))
print(solution(2,1,2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1,1,5 ,["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1,1,1, ["23:59"]))
print(solution(10,60,45,["23:59", "23:59", "23:59", "23:59", "23:59", "23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59","23:59", "23:59", "23:59", "23:59"]))



    