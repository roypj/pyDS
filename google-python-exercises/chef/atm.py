w= input()
withdrawal,balance=w.split()
withdrawal = float(withdrawal)
balance = float(balance)
fee = 0.50

if((withdrawal>0 and withdrawal<=2000)and(balance>0 and balance<=2000)):
    if(withdrawal%5==0 and (withdrawal+fee<balance)):
        print('%.2f'%(balance-withdrawal-fee))
    else:
        print('%.2f'%balance)

   
