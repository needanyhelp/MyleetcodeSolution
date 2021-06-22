
adjacencyList={
    'a':['b','c','d'],
    'b':['e','f'],
    'c':['g'],
    'd':['h'],
    'e':['k','i'],
    'f':['i'],
    'g':[],
    'h':[],
    'k':[],
    'i':[]
}


def dfsStack():

    global adjacencyList

    visited=[]
    stack=[]
    
    def reculsive(list):


        for k in list:
            stack.append(k)
        
        while stack:                
            a=stack.pop()
            visited.append(a)

            for k in adjacencyList[a]:
                if k not in visited:
                    stack.append(k)

        print(visited)


            

    
    reculsive(adjacencyList['a'])


dfsStack()
