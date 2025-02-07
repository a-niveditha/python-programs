s=input().split()
word=s[0]
no=int(s[1])
L=[]
for i in word:
    L.append(i)
L.sort()
a=['n']*no
def fn(l,n,a):
    if n==2:
        for i in range(len(l)):
            for j in range(len(l)):
                if i!=j:
                    #print(a,'before updation')
                    a[-1]=l[j]
                    a[-2]=l[i]
                    for k in a:
                        print(k,end='')
                    print()
    elif n==1:
        for i in l:
            print(i)
    else:
        for i in range(len(l)):
            #print(l[i],end='')
            l1=l.copy()
            c=l1.pop(i)
            a[no-n]=c
            fn(l1,n-1,a)

fn(L,no,a)
