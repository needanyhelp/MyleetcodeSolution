
adjacencyList={
    'a':['b','c','d'],
    'b':['e','f'],
    'c':['g'],
    'd':['h'],
    'e':['k'],
    'f':[],
    'g':[],
    'h':[],
    'k':[]
}


def dfsReculsive():

    global adjacencyList

    visited=[]

    def reculsive(list):
        for k in list:
            if k not in visited:
                visited.append(k)
            reculsive(adjacencyList[k])

            

    
    reculsive(adjacencyList['a'])


dfsReculsive()
