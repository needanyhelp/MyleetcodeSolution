def solution(n, arr1, arr2):
    c=[]
    for i in range(n):
        c.append(bin(arr1[i]|arr2[i]))
    
    d= list(map(str,c))

    for i in range(n):
        d[i]=d[i][1:].replace("1","#")
        d[i]=d[i][1:].replace("0"," ")
        
    
    
    print(d)
    
solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])