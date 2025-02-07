#for 2 digit number
'''def check(n):
    m=n
    a=n//10
    while True :
        s=a+b
        if s==m:
            print('success')
            break
        a,b=b,s
        if s>100:
            print('failure')
            break
n=int(input('enter'))
check(n)'''

'''keith number- example - 14
1+4=5, 4+5=9 , 5+9=14- success

for 3 digit numbers- 197
1+9+7=17, 9+7+17=33 .....'''


# for 3 digit number
'''n=int(input('enter number'))
l=[]
m=n
while n!=0:
    l.append(n%10)
    n//=10
a,b,c=l[2],l[1],l[0]
while True :
        s=a+b+c
        #print(s)
        if s==m:
            print('success')
            break
        a,b,c=b,c,s
        if s>1000:
            print('failure')
            break'''

#permutation of 2 letters from a word
s=input().split()
word=s[0]
no=s[1]
l=[]
for i in word:
    l.append(i)
l.sort()
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j:
            print(l[i],l[j])
