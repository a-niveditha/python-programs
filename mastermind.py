import random

#generating first attempt
L=['A','B','C','D','E','F']

l=[]
while len(l)<4:
    i=random.randrange(0,6)
    k=L[i]
    if k not in l:
        l.append(k)
print(l)
#l is the chosen sequence

while True :
    ch=input('enter choice')
    caps=ch.upper()
    black=white=0
    for i in range(0,4):
        if caps[i] in l :
            if caps[i]==l[i]:
                white+=1
            else:
                black+=1
    print( 'black: ',black , 'white:',white)
    if white==4:
        print('game over')
