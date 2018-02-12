def factorial(num):
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)

t = int(input())
for num in range(t):
    factnum=int(input())
    print(factorial(factnum))
