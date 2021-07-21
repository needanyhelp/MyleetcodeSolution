import math

def solution(str1, str2):
    setA=[]
    setB=[]
    str1=str1.lower()
    str2=str2.lower()

    for i in range(len(str1)-1):
        if str1[:2].isalpha()!=True:
            str1=str1[1:]
            continue
        else:
            setA.append(str1[:2])       
        str1=str1[1:]

    for i in range(len(str2)-1):
        if str2[:2].isalpha()!=True:
            str2=str2[1:]
            continue
        else:
            setB.append(str2[:2])       
        str2=str2[1:]

    intersection = []

    copy_A= setA.copy()
    copy_B= setB.copy()


    for i in range(len(setA)):
        if copy_A[i] in copy_B:
            intersection.append(copy_A[i])
            copy_B.pop(copy_B.index(copy_A[i]))
            

    unionSet=setA+setB

    for i in range(len(intersection)):
        if intersection[i] in unionSet:
            unionSet.pop(unionSet.index(intersection[i]))

    if len(intersection)*len(unionSet)==0:
        return 65536*1

    return math.floor((len(intersection)/len(unionSet))*65536)




solution('aa1+aa2', 'AAAA12')
