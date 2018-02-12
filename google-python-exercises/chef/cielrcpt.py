#find closest power of 2 less than or equal to N
def closestPwr(num):
    if num>0:
        i=0
        while(2**i<=num and i<12):
            i+=1
        return 2**(i-1)

testCases = int(input())
for t in range(testCases):
    p = int(input())
    menu =0
    while(p>0):
        p=max(p-closestPwr(p),0)
        menu+=1
    print(menu)
    
