import collections

route={
    'a':['b','c'],
    'b':['d'],
    'c':['e','f','g'],
    'd':[],
    'e':[],
    'f':[],
    'g':[],
}

def bfs(start):
    queue=collections.deque()

    visited=[]
    visited.append(start)

    queue.append(start)

    while queue:
        adjacentNode=queue.popleft()
        for i in route[adjacentNode]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

    print(visited)


