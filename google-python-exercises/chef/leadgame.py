N = int(input())
p1scr=[]
p2scr=[]
leads=[]
for n in range(N):
    p1,p2=map(int,input().split())
    p1scr.append(p1)
    p2scr.append(p2)
cumScrP1 = [sum(p1scr[0:i+1]) for i in range(len(p1scr))]
cumScrP2 = [sum(p2scr[0:i+1]) for i in range(len(p2scr))]
cumScrP1 = list(map(int,cumScrP1))
cumScrP2 = list(map(int,cumScrP2))
absleads = [abs(p1-p2) for p1,p2 in zip(cumScrP1,cumScrP2)]
leads = [p1-p2 for p1,p2 in zip(cumScrP1,cumScrP2)]
winLead = max(absleads)
win = leads[absleads.index(winLead)]
if win>0:
    print (1,winLead)
else:
    print(2,winLead)
    





