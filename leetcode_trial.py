'''x=252
number=str(x)
l=len(number)
for i in range(l):
     if number[i]!=number[l-i-1]:
          print("no")
          break
else:
     print("yes")'''

i=0
divisor=3
dividend=15
num=divisor
if divisor<0:
     divisor=(-1)*divisor
val=divisor
while val<dividend:
     print(i,val)
     i+=1
     val+=divisor
if(dividend<0 or num<0 ):
     print((i)*(-1))
else:
     print(i)
          
