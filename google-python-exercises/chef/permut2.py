#time limit exceeded
'''while (int(input())!=0):    
    permut = list(map(int,input().split()))
    flag=1
    for i in range(len(permut)):
        if ((permut.index(i+1)+1)!=permut[i]):
            flag=0
            break
    if(flag==0):
        print("not ambiguous")          
    if(flag==1):
        print("ambiguous")'''

while(int(input())!=0):
    permut = list(map(int,input().split()))
    invPer=[0]*len(permut)
    #print(invPer)
    for i in range(len(permut)):
        #print("i+1 - "+str(i+1))
        #print("idx of inv - "+str(permut[i]-1))
        invPer[permut[i]-1]=i+1
    if permut==invPer:
        print("ambiguous")
    else:
        print("not ambiguous")

       
        
    


