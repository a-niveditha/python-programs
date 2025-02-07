n=int(input())
l=[]
for i in range(n):
    s=input().split()
    l.append(s)
for i in l:
    d={}
    c=0
    for j in i:
        l1=[]
        n=()
        for k in j:
            l1.append(k)
        l1.sort()
        n=tuple(l1)
        d[c]=n
        c+=1
t=()
for i in d:
    for j in d:
        if d[i]==d[j]:
            if i not in t:
                t+=(d[j]),
a={}
for i in t:
    if i not in a:
        a[i]=(t.count(i))**0.5
p=sorted(a.values(),reverse=True)
for i in p:
    print(i,end=' ')
    


        
        
        
