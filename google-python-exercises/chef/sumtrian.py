def reduceTriangle(triangle):
    newRow=[]
    if (len(triangle)>1):
        lstRow = triangle[-1]
        #print(lstRow)
        lb1Row = triangle[-2]
        #print(lb1Row)
        for i in range(len(lb1Row)):
            maxSum = max((lb1Row[i]+lstRow[i]),(lb1Row[i]+lstRow[i+1]))
            #print(maxSum)
            newRow.append(maxSum)
        #print(newRow)
        redTrian = triangle[0:len(triangle)-2]
        redTrian.append(newRow)
        #print(redTrian)
    return redTrian

testCases = int(input())

for n in range(testCases):
    numLines = int(input())
    triangle = []
    for line in range(numLines):
        triangle.append(input())
    triangle=[list(map(int,entry.split())) for entry in triangle]
    while(len(triangle)>1):
        triangle = reduceTriangle(triangle)
    #[map(int,x) for x in triangle]
    print(triangle[0][0])



        
