def binary_search(n,S,x):
    low = 1
    high = n
    location = 0
    if S[len(S)-1] < x or S[0]> x:
        print('not search number!!')
        exit(0)
    while (low<=high) and (location == 0):
        mid = (low+high) // 2
        if x == S[mid]:
            location = mid
        elif x < S[mid]:
            high = mid - 1
        elif x > S[mid]:
            high = mid + 1
      
            
    return location

num = [1,5,8,9]
print('위치한 인덱스 번호는 ',binary_search(len(num), num,50))
