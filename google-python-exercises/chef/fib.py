fib = []
fib.append(0)
fib.append(1)
n = 10
for i in range(2,n,1):
    fib.append(fib[i-2]+fib[i-1])
'''print(fib)'''

def fib(n):
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(1,n):
        print(first+second)
        temp = second
        second = first+second
        first = temp
    
    
