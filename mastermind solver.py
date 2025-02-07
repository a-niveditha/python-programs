L=['A','B','C','D','E','F']
ans=[]
global L
global ans 
#w=white,b-black

def sum2():
    for i in L:
        if i not in l:
            ans.append(i)
    
    if w==2: #considering the choice to be the left out letters  in the 1st 2 positions and the last 2 letters of prev guess in the same position
          k=l[2]
          ans.append(k)
          m=l[3]
          ans.append(m)
    if  w==1: #
        
def sum3():
    
def sum4():


#1st attempt
l=[]
while len(l)<4:
    i=random.randrange(0,6)
    k=L[i]
    if k not in l:
        l.append(k)
print(l)
w=int(input('enter no of white '))
b=int(input('enter no of black '))
if w+b=2:
    sum2()
elif w+b=3:
    sum3()
elif w+b=4:
    sum4()


    
