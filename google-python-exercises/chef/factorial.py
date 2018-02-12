num_inputs =int(input())
#num_inputs=[3,60,100,1024,23456,8735373]
for nums in range(num_inputs):
#for num in num_inputs:
    num = int(input())
    i=1
    cnt=0
    while(num//(5**i)>=1):
        cnt+=(num//(5**i))
        i+=1
    print(cnt)
