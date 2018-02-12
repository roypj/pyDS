testCases = int(input())

for t in range(testCases):
    sumdigits=0
    num = int(input())
    while(num>0):
        sumdigits+=num%10
        num = num//10
    print(sumdigits)
