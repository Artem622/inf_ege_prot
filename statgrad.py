'''def f(x,y,n =frozenset()):
    if x==y:
        return 1
    elif abs(x)>50 or x in n:
        return 0
    res=0
    for s in (x+2,x-3):
        res+=f(s,y,n|{x})
    return res
print(f(1,30))'''

'''import itertools

a=list(itertools.product('АЕПСТУХ',repeat=4))
k=0
for i in range(len(a)):
    s=''.join(a[i])
    if i  > 999 and s[0]!= s[1] and s[1]!=s[2] and s[2]!=s[3]:
        k+=1
print(k)'''

'''for i in range(101,120):
    a='3'*i
    while '111' in a or '333' in a:
        if '111' in a:
            a=a.replace('111','3',1)
        else:
            a=a.replace('333','1',1)
    print(a,i)'''

'''def vodka(x,a,b):
    s=''
    x=int(str(x),a)
    while x>0:
        s=s+str(x%b)
        x=x//b
    return s[::-1]

A=set()
for x in range(100):
    var=vodka(3 * 16**2018 - 2 * 8** 1028 - 3 * 4 **1100 - 4** x -2022,10,4)
    var=int(var)
    if var>0:
        s=sum(map(int,str(var)))
        A.add(s)
print(len(A))'''
'''print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((y or x)==(y<=w)) or z)==0:
                    print(x,y,z,w)
'''

'''for N in range(10000):
    binn=bin(N)[2:]
    if binn.count('1')%2==0:
        binn='1'+binn+'00'
    else:
        binn='11'+binn
    var=int(binn,2)
    if var>=412:
        print(N)'''

'''def f(s):
    s=(s+31)//26
    n=813
    while s>0:
        n=n//3
        s=s-n
    return n

for s in range(2,1000000):
    if f(s)==30:
        print(s)'''
'''from functools import lru_cache
@lru_cache(None)
def f(n):
    if n<3:
        return 1
    if n>2 and n%2==0:
        return g(n)+f(n-1)
    if n>2 and n%2==1:
        return f(n-2)-2*g(n+1)
def g(n):
    if n<3:
        return 1
    if n>2 and n%2==0:
        return f(n-3)+f(n-2)
    if n>2 and n%2==1:
        return f(n+1)-g(n-1)

print(g(120))'''

'''a=list(map(int,open("C:\\Users\\Artem\\Music\\17.txt").readlines()))
k=0
maxx=0
eblan=0
for i in a:
    i=abs(i)
    xui=str(i)
    pizda=xui[0]
    eblan+=int(pizda)
for i in range(len(a)-1):
    if a[i]*a[i+1]>eblan:
        k+=1
        maxx=max(maxx,a[i]+a[i+1])
print(k,maxx)
'''
'''from functools import lru_cache

def moves(h):
    x,k=h
    a=[]
    if k!=0:
        a+=[(x+1,0)]
    if k!=1:
        a+=[(x+2,1)]
    if k!=2:
        a+=[(x+3,2)]
    if k!=3:
        a+=[(x*2,3)]
    if k!=4:
        a+=[(x*3,4)]
    if k!=5:
        a+=[(x*x,5)]
    return a

@lru_cache(None)
def game(h):
    x,k=h
    if x>=250:
        return 'W'
    if any(game(m)=='W' for m in moves(h)):
        return 'P1'
    if all(game(m)=='P1' for m in moves(h)):
        return 'B1'
    if any(game(m)=='B1' for m in moves(h)):
        return 'P2'
    if all(game(m)=='P1' or game(m)=='P2' for m in moves(h)):
        return 'B2'
for i in range(1,250):
    h = i,-1
    print(i,game(h))'''

'''A=[]
for i in range(-1000,100000):
    s = i
    s = (s + 21) // 43
    p = 12
    q = 8
    K1 = 0
    K2 = 0
    while s <= 100:
        s = s + p
        K1 = K1 + 1
    while s >= q:
        s = s - q
        K2 = K2 + 1
    K1 += s
    K2 += s
    if K1 == 13 and K2 == 17:
        A.append(i)
print(len(A))'''


'''f=open("C:\\Users\\Artem\\Music\\24.txt")
a=f.read()
f.close()
a=a.replace('AA','*')
a=a.replace('CC','*')
k=0
maxx=0
for i in range(len(a)-1):
    if a[i]=='*' :
        k+=1
        maxx=max(maxx,k)
    else:
        k=0
print(maxx)'''

'''v=[0]
for i in range(1,10**9):
    a=list(str(i))
    s=len(a)
    if a[0] == '1' and a[s-1] == '9' and '5' in a:
        a.sort()
        a=list(map(int,a))
        a=set(a)
        a=int(''.join(map(str,a)))
        if a%21 == 0 and a not in v:
            print(a,a//21)
            v.append(a)'''

'''f=open("C:\\Users\\Artem\\Music\\26.txt")
N=int(f.readline())
A=[]
for i in range(N):
    x,y=f.readline().split()
    A.append((int(x),int(y)))
A.sort( key=lambda i:(-(i[0]),(i[1])))
for i in range(len(A)-1):
    if A[i+1][1]-A[i][1]==21:
        print(A[i][0],A[i][1]+1)
        break'''
