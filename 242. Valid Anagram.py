def solution(s, t):
    s= sorted(s)
    t= sorted(t)

    if s==t:
        return True
    else :
        return False


print(solution("anagram","nagaram"))