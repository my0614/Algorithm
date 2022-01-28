def bin_search(S,x, high, low):
    if S[0] < x or S[len(S)-1] < x:
        print('원하는 숫자가 없습니다.')
        return -1
    mid = (low + high) // 2
    if S[mid] > x:
        high = S[mid-1]
        return bin_search(S, x, high, low)
    elif S[mid] < x:
        low = S[mid+1]
        return bin_search(S, x, high, low)
    else:
        return mid
    
    
    

S = [1,3,4,5,6,7]

print('위치한 인덱스는',bin_search(S, 12, len(S), 1))
