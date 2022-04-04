'''for i in range(700001,10000000):
    A=[]
    M=0
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
            break
    if len(A)>0:
        r=i/A[0]
        A.append(r)
    if len(A)==2:
        M=A[0]+A[1]
    if M%10==8:
        print(i,M)'''
'''
24
for i in range(452022,1000000):
    A=[]
    M=0
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
            break
    if len(A)>0:
        r=i/A[0]
        A.append(r)
    if len(A)==2:
        M=A[0]+A[1]
    if M%7==3:
        print(i,M)'''

'''
xz
def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
for i in range(101000000, 102000001, 2):
    if (i // 2) ** 0.5 == int((i // 2) ** 0.5):
        if isprime((i // 2) ** 0.5)==1:
            print(i)'''


'''
19

for i in range(2000000,3000001):
    A=[]
    delit=[]
    v_delit=[]
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            delit.append(j)
            v_delit.append(i/j)
    for x in range(len(delit)):
        if abs(delit[x]-v_delit[x])<=115:
            A.append(abs(delit[x]-v_delit[x]))
    if len(A)>=3:
        print(i)
'''

'''
17
for i in range(289123456,389123457):
    k=0
    d=2
    n=0
    if int(i**0.5)==i**0.5:
        while d**2<i:
            if i%d==0:
                k+=2
                if n==0:
                    n=i//d
            d+=1
    if k==2:
        print(i,n)
'''
'''
16
for i in range(123456789, 223456790):
    k=0
    d=2
    max_del=0
    if int(i**0.5) == i**0.5:
        while d**2 < i:
            if i%d == 0:
                k += 2
                if max_del == 0:
                    max_del = i // d
            d += 1
    if k == 2:
        print(i,max_del)
'''
'''
15
ch=0
maxk=0
for i in range(568023,569231):
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
    if len(A)>maxk:
        maxk=len(A)
        ch=i
print(maxk,ch)
'''

'''
14
for i in range(125256,125331):
    A=[]
    for f in range(2,i+1,2):
        if i % f==0:
            A.append(f)
        if len(A)>6:
            break
    if len(A)==6:
        print(*A)
'''
'''
12
def pri(i):
    d=2
    while d**2<=i:
        if i%d==0:
            return False
        d+=1
    return True

k=0
for i in range(2422000,2422081):
    k+=1
    if pri(i)==1:
        print(k,i)'''
'''
9
ch=0
maxdel=0
for i in range(84052,84131):
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
    if len(A)>maxdel:
        maxdel=len(A)
        ch=i
print(maxdel,ch)'''
'''
3
for i in range(210235,210301):
    A=[]
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
        if len(A)>4:
            break
    if len(A)==4:
        print(A)'''

'''
2
def f(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

k=0
for i in range(245690,245756):
    k+=1
    if f(i)==1:
        print(k,i)


'''
'''
1
for i in range(174457,174506):
    A=[]
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
        if len(A)>2:
            break
    if len(A)==2:
        print(*A)'''


'''
5 ебучих нечетных делителей
def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
for i in range(35000000, 40000000 + 1):
    a = i
    while a % 2 == 0:
        a = a // 2
    if (a ** 0.25) == int(a ** 0.25):
        if isprime(a ** 0.25)==1:
            print(i)'''

'''
3 ебучих четных делителя

def isprime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
for i in range(101000000, 102000000 + 1, 2):
    if (i // 2) ** 0.5 == int((i // 2) ** 0.5):
        if isprime((i // 2) ** 0.5):
            print(i)
'''

'''

три нетривиальных делителя+наибольший такой делитель

def f(i):
    d=2
    while d**2<=i:
        if i%d==0:
            return False
        d+=1
    return True

for i in range(289123456,389123457):
    if (int(i**0.25)==i**0.25) and f(i**0.25)==1:
        tr=0
        for j in range(int(i**0.25)+1,1,-1):
            if i%j==0:
                tr=j
                break
        print(i,i//tr)
'''


'''count=0
for i in range(452022,1000000000):
    M=0
    for j in range(2,i//2+1):
        if i%j==0:
            M+=j
            break
    for k in range(i//2+1,2,-1):
        if i%k==0:
            M+=k
            break
    if M%7==3 and count<5:
        count+=1
        print(i,M)'''


'''count=0
for i in range(600001,1000000000):
    delit=0
    for j in range(2,i//2+1):
        if i%j==0 and j!=7 and j%10==7:
            delit=j
            break
    if delit!=0 and count<5:
        count+=1
        print(i,delit)
'''