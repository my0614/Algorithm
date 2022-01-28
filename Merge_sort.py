def mergesort(S):
    n = len(S)
    if (n <= 1):
        return S

    else:
        mid = n // 2
        S1 = mergesort(S[:mid])
        S2 = mergesort(S[mid:])
        return merge(S1,S2)
    
def merge(S1, S2):
    S = []
    i = j = 0
    while (i < len(S1)) and (j < len(S2)):
        if (S1[i] < S2[j]):
            S.append(S1[i])
            i+=1
        else:
            S.append(S2[i])
            j+=1

    if i<len(S1):
        S += S1[i:len(S1)]
        print(S)
    else:
        S += S2[j:len(S2)]
        print(S)

    return S
    
S = [1,10,20,30,50,55,100]
mergesort(S)
