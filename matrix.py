
r=int(input('enter no of rows and columns'))
A=[]
B=[]
for i in range(r):
    l=[]
    for j in range(r):
        print('first matrix: enter value for element:',i,j)
        a=int(input())
        l+=[a]
    A+=[l]
for i in range(r):
    l=[]
    for j in range(r):
        print('second matrix: enter value for element:',i,j)
        a=int(input())
        l+=[a]
    B+=[l]
print('First matrix:',A)
print('Second matrix:',B)

#addition
C=[]
for i in range(r):
    l=[]
    for j in range(r):
        element=A[i][j]+B[i][j]
        l+=[element]
    C+=[l]
print('Sum of A and B:',C)

#multiplication
D=[]
for i in range(r):
    l=[]
    for j in range(r):
        e=0
        for k in range(r):
            e+=A[i][k]*B[k][j]
        l+=[e]
    D+=[l]
print('Product of A and B:',D)

#transpose of A and B
T1=[]
for p in range(r):
    l=[]
    for q in range(r):
        l+=[0]
    T1+=[l]
T2=T1

for i in range(r):
    for j in range(r):
        T1[j][i]=A[i][j]
print('Transpose of A:',T1)

for i in range(r):
    for j in range(r):
        T2[j][i]=B[i][j]
print('Transpose of B:',T2)

  
        
