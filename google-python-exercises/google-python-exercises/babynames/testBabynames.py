import sys
import re
f = open('baby1990.html','rU')
nmDat=f.read()
#print(nmDat)
f.close()
#extract year
pattern = r'Popularity in (\d\d\d\d)'
yrMtch = re.search(pattern,nmDat)
year = yrMtch.group(1)
#extract rank and names
'<td>1</td><td>Michael</td><td>Jessica</td>'
nmPtrn = r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
rnkMtch = re.findall(nmPtrn,nmDat)
lst=[]
for s in rnkMtch:
    bNm = s[1]+' '+s[0]
    lst.append(bNm)
    gNm = s[2]+' '+s[0]
    lst.append(gNm)
lst = sorted(lst,key=lambda s:s[0])
lst.insert(0,year)
text = '\n'.join(lst)+'\n'
print(text)
opF = open('op.txt','w')
for line in text:
    opF.write(line)
opF.close()
sys.exit(0)
