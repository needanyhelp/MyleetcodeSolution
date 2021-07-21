from typing import List
import collections

def solution(s, t):
    if not(s and t):
        return False

    window_size=len(t)
    i=0
    
    while True:
        next=0

        if(window_size>len(s)):
            return False

        if(i==len(s)-window_size+1):
            i=0
            window_size+=1 
            continue

        temp=s[i:i+window_size]
        for j in range(len(t)):
            if t[j] not in temp:
                next=1
                break
          
        if next==1:
            i+=1
            continue
        

        #when found
        return temp



print(solution("ABCDEFG", "F"))