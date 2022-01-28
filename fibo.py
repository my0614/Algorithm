import time
def fibo(n):
    f = [0] * (n+1)
    if  n > 0:
        f[1] = 1

        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]
    return f
def fibo2(n):
    a = 0
    b = 1
    result = 0
    print(a,b, end=' ')
    if n>0:
        #print('1')
        for i in range(2,n+1):
            result = a + b
            print(result, end = ' ')
            a = b
            b = result
            
   
print(fibo2(10))
