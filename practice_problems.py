'''s=input('enter sequence').upper()
l=['B','R','G']
l.sort()
for i in range(len(s)):
    str=s[i:i+3]
    g=[i for  i in str]
    g.sort()
    if g==l:
        print(i)

d={}
n=int(input())
for i in range(n):
    s=input().split()
    if s[0] in d:
        d[s[0]].append(int(s[1]))
    else:
        d[s[0]]=[int(s[1])]
for i,v in d.items():
    print(i,sum(v)/len(v))'''

'''s=list(input('enter string'))
l1=[chr(i) for i in range(65,91)]
l2=[chr(i) for i in range(97,123)]
for i in s:
    if i.isupper():
        ind=l1.index(i)
        print(l1[(ind+3)%26],end='')
    elif i.islower():
        ind=l2.index(i)
        print(l2[(ind+3)%26],end='')

l=[1,3,5]
l1=[]
for i in range(len(l)):
    s=0
    for j in range(i+1):
        s+=l[j]
    l1.append(s)
print(l1)

s1='today is a wednesday'
s2='today is so boring coz its a wednesday'
#print(s1.title())
ch=input('enter substring')
if ch in s1:
    l=s1.split(ch)
    print(l)
    print(l[0],ch.title(),l[1])

n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
for uid in lst:
    l=[]
    d,u=0,0
    for i in uid:
        l.append(i)
        if l.count(i)>1:
            print('Invalid')
            break
        else:
            if len(uid)!=10:
                print('Invalid')
                break
            else:
                if i.isalpha():
                    if i.isupper():
                        u+=1
                elif i.isdigit():
                    d+=1
                else:
                    print('Invalid')
                    break
    else:
        if u>1 and d>2:
            print('Valid')
        else:
            print('Invalid')'''

'''n=int(input())
l=[input() for _ in range(n)]
a=' && '
b=' || '
for i in l:
    j=i
    if a in i:
        j=i.replace(a,' and ')
        if b in i:
            k=j.replace(b,' or ')
    else:
        if b in i:
            k=i.replace(b,' or ')
        
    print(k)'''

    
'''import re
for i in l:
    a=re.search(' && ',i)
    print(a)'''

'''n=int(input())
l=[]
for i in range(n):
    l.append(input())
for i in l:
    try:
        print(int(i[0])//int(i[2]))
    except ZeroDivisionError :
        print('Error Code: integer division or modulo by zero')
    except ValueError:
        if i[0].isdigit():
            print(f"Error Code: invalid literal for int() with base 10: '{i[2]}'")
        else:
            print(f"Error Code: invalid literal for int() with base 10: '{i[0]}'")'''

l=input().split()
k,m=int(l[0]),int(l[1])
d=[]
for i in range(k):
    a=input().split()
    a.pop(0)
    b=[]
    for i in a:
        b.append(int(i))
    d.append(b)
s=0
for i in d:
    s+=(max(i)**2)
print(s%m)
