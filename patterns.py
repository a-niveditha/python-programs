#pyramid
'''n=int(input())
for i in range(int((n+1)/2)):
    a=int((n-1)/2)
    print(' '*(a-i),end='')
    print('@'*(2*i+1))'''

#diamond
'''n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),'* '*i)
for i in range(n-1,-1,-1):
    print(' '*(n-i),'* '*i)'''

#letter pyramid
'''n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    j=0
    for j in range(97+i-1,97,-1):
        print(chr(j),end='')
    for j in range(97,97+i):
        print(chr(j),end='')
    print()'''
        
'''n=int(input('no of lines'))
for i in range(1,n+1):
    for j in range(97,97+i):
        print(j,end='')
    print(' '*  '''
        
#letter rangoli
'''def print_rangoli(n):
    for i in range(1,n+1):
        print('-'*((n-i)*2),end='')
        for j in range(96+n,96+n-i,-1):
            print(chr(j),'-',sep='',end='')
        for j in range(98+n-i,97+n):
            if j==96+n:
                print(chr(j),end='')
            else:
                print(chr(j),'-',sep='',end='')
        if i==1:
            print('-'*((n-i)*2-1),end='')
        else:
            print('-'*((n-i)*2),end='')
        print()
    for i in range(n-1,0,-1):
        print('-'*((n-i)*2),end='')
        for j in range(96+n,96+n-i,-1):
            print(chr(j),'-',sep='',end='')
        for j in range(98+n-i,97+n):
            if j==96+n:
                print(chr(j),end='')
            else:
                print(chr(j),'-',sep='',end='')
        if i==1:
            print('-'*((n-i)*2-1),end='')
        else:
            print('-'*((n-i)*2),end='')
        print()
n=int(input())
print_rangoli(n)'''



