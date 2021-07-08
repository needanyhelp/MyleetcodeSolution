import collections

def solution(cities, cacheSize):
    cache = collections.deque([])
    time=0

    for city in cities:
        city=city.lower()
        #hit
        if city in cache:
            time+=1
            cache.remove(city)
            cache.appendleft(city)
        
        #miss
        else:
            time+=5
            if cacheSize==0:
                continue

            if len(cache)==cacheSize:
                cache.pop()
            cache.appendleft(city)
        
    print(time)


solution(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul",
"NewYork", "LA"], 3)
solution(["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo",
"Seoul"], 3)
solution(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul",
"Rome", "Paris", "Jeju", "NewYork", "Rome"], 2)
solution(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul",
"Rome", "Paris", "Jeju", "NewYork", "Rome"], 5)
solution(["Jeju", "Pangyo", "NewYork", "newyork"], 2)
solution(["Jeju", "Pangyo", "Seoul", "NewYork", "LA"],0)