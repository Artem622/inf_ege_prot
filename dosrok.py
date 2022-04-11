'''#2
# ¬(𝑥 → 𝑧) ∨ (𝑦 ≡ 𝑤) ∨ ¬y
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(x <= z) or (y == w) or not(y)) == 0:
                    print(x,y,z,w)
                    #=xzyw
                    '''
'''#5
for n in range(1,1000000):
    binn=bin(n)[2:]
    if n%2==0:
        binn=binn+'10'
    else:
        binn= '1'+binn+'01'
    x=int(binn,2)
    if x>516:
        print(n)
        break'''

'''for i in range(1,10000000):
    s=i
    s = (s - 10) // 7
    n = 1
    while s > 0:
        n = n*2
        s = s - n
    if n == 8:
        print(i)
        break'''
'''import itertools

a=list(itertools.product('АПРСУ',repeat=5))
k=0
bad=['АА']
for i in a:
    k+=1
    s=''.join(i)
    for j in bad:
        if j in s:
            break
        elif s[0]=='У':
            print(k)'''

'''a='8'*86
while '1111' in a or '8888' in a:
    if '1111' in a:
        a=a.replace('1111','8',1)
    else:
        a=a.replace('8888','11',1)
print(a)
'''

'''def vodka(x,a,b):
    s=''
    x=int(str(x),a)
    while x>0:
        s=s+str(x%b)
        x=x//b
    return s [::-1]

ds=vodka(3*16**2018-2*8**1028-3*4**1100-2**1050-2022,10,4)
print(ds.count('3'))'''

'''def f(n,m):
    return n%m==0

A=0
while True:
    for x in range(1,100000):
        if not((f(x, 3) <= (not(f(x, 5))) or (x + A >= 70))):
            break
    else:
        print(A)
    A+=1'''

'''def f(n):
    if n<3:
        return 2
    if n>2 and n%2==0:
        return f(n-1)+f(n-2)-n
    if n>2 and n%2==1:
        return f(n-2)-f(n-1)+2*n

print(f(30))'''

'''data=list(map(int,open("C:\\Users\\Artem\\Downloads\\dosrok17.txt").readlines()))
A=[]
count=0
maxx=0
for i in data:
    if i%17==0:
        A.append(i)
minn=min(A)
for j in range(len(data)-1):
    if (data[j]%minn==0) or (data[j+1]%minn==0):
        count+=1
        maxx=max(maxx,data[j]+data[j+1])
print(count,maxx)'''

'''from functools import lru_cache

def moves(s):
    (a,b)=s
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

@lru_cache(None)
def game(s):
    if s[0]<=1 or s[1] <=1:
        return
    if sum(s) >=223:
        return 'W'
    if any(game(m)=='W' for m in moves(s)):
        return 'P1'
    if any(game(m)=='P1' for m in moves(s)):
        return 'B1'
    if any(game(m)=='B1' for m in moves(s)):
        return 'P2'
    if all(game(m)=='P1' or game(m)=='P2' for m in moves(s)):
        return 'B2'

for s in range(1,206):
    if game((17,s)) is not None:
        print(s,game((17,s)))'''

'''from functools import lru_cache

def moves(s):
    (a,b)=s
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

@lru_cache(None)
def game(s):
    if s[0]<=1 or s[1] <=1:
        return
    if sum(s) >=223:
        return 'W'
    if any(game(m)=='W' for m in moves(s)):
        return 'P1'
    if all(game(m)=='P1' for m in moves(s)):
        return 'B1'
    if any(game(m)=='B1' for m in moves(s)):
        return 'P2'
    if all(game(m)=='P1' or game(m)=='P2' for m in moves(s)):
        return 'B2'

for s in range(1,206):
    if game((17,s)) is not None:
        print(s,game((17,s)))'''


'''for i in range(1,100000):
    s = i
    P = 10
    Q = 8
    K1 = 0
    K2 = 0
    while s <= 100:
        s = s + P
        K1 = K1 + 1
    while s >= Q:
        s = s - Q
        K2 = K2 + 1
    K1 += s
    K2 += s
    if K1==10 and K2==19:
        print(i)
'''

'''def f(x,end):
    if x>end:
        return 0
    if x==end:
        return 1
    return f(x+2,end)+f(x*2,end)

print(f(1,16)*f(16,52))'''

'''f=open("C:\\Users\\Artem\\Downloads\\dosrok24.txt")
a=f.read()
f.close()
counter=0
maxx=0
for i in range(1,len(a)-2,2):
    if (a[i]=='A' and a[i-1]=='B') or (a[i]=='A' and a[i-1]=='C'):
        counter+=1
    else:
        maxx=max(maxx,counter)
        counter=0
print(maxx)'''
'''a=open("C:\\Users\\Artem\\Downloads\\dosrok24.txt").readline()

a=a.replace('AB','*')
a=a.replace('AC','*')
count=0
maxx=0
for i in range(len(a)):
    if a[i]=='*':
        count+=1
        maxx = max(maxx, count)
    else:

        count=0
print(maxx)'''

'''A=[]
for i in range(123450000,123460000):
    s=str(i)
    if s[6]=='6' and s[8]=='8' and i%17==0:
        A.append(i)
        A.append(i//17)
print(A)'''

'''f=open("C:\\Users\\Artem\\Downloads\\dosrok26.txt")
N=int(f.readline())
A=[]
for i in range(N):
    x,y=f.readline().split()
    A.append((int(x),int(y)))
A.sort( key=lambda i:(-(i[0]),(i[1])))
for i in range(len(A)-1):
    if A[i+1][1]-A[i][1]==12:
        print(A[i][0],A[i][1]+1)
        break'''

'''f = open("C:\\Users\\Artem\\Downloads\\dosrok27B.txt")
N=int(f.readline())

a=[]
for i in range(N):
    a.append((int(f.readline())))
s_l=s_r=0
s= [0]*N
for i in range(1,N//2):
    s[0]+=a[i]*i+a[-i]*i
    s_l+=a[-i]
    s_r+=a[i]
s[0]+=a[N//2]*(N//2)
for i in range(1,N):
    s[i]=s[i-1] -s_r - a[(N//2+i-1)%N]+s_l+a[i-1]
    s_l=s_l-a[(N//2+i)%N]+a[i-1]
    s_r=s_r-a[i]+a[(N//2+i-1)%N]
m=float('inf')
for i in range(len(s)):
    if s[i]<m:
        m=s[i]
        ind=i+1
print(ind)'''






