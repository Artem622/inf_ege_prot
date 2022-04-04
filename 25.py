'''def f(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

x = 35000000
y = 40000000
A=[]
for j in range(3, int(y ** (0.25)) + 1):
    if f(j)==1:
        l = j ** 4
        while l <= y:
            if l >= x and l <= y:
                A.append(l)
            l *= 2
print(sorted(A))

'''
'''for i in range(10000001,1000000000):
    A=[]
    for j in range(i//2+1,2,-1):
        if i%j==0:
            A.append(j)
        if len(A)>2:
            break
    if len(A)==2:
        if sum(A)>0 and sum(A)<10000:
            print(sum(A))'''
'''def isprime(n):
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
'''for i in range(200000001,3000000000):
    s=1
    k=0
    for j in range(2,i//2+1):
        if i%j==0:
            k+=1
            s=s*j
        if k==5 and s<i:
            print(s)
            break

'''
'''vaxdel=0
chis=0
for i in range(84052,84131):
    delka=0
    for j in range(1,i+1):
        if i%j==0:
            delka+=1
    if delka>vaxdel:
        vaxdel=delka
        chis=i
print(vaxdel,chis)'''

'''a=210235
b=210300
for i in range(a,b+1):
    A=[]
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
        if len(A)>4:
            break
    if len(A)==4:
        print(*A)'''


'''#1
for i in range(174457,174506):
    A=[]
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
            if len(A)>2:
                break
    if len(A)==2:
        print(*A)'''


'''#2
num=0
for i in range (245690,245757):
    num+=1
    A=[]
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
        if len(A)>0:
            break
    if len(A)==0:
        print(num,i)'''




'''#3
for i in range(210235,210301):
    A=[]
    for j in range(2,i//2+1):
        if i%j==0:
            A.append(j)
        if len(A)>4:
            break
    if len(A)==4:
        print(*A)
'''

'''#4
for i in range(185311,185331):
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
        if len(A)>4:
            break
    if len(A)==4:
        print(*A)'''

'''#5   312614,312652
for i in range(312614,312652):
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
        if len(A)>6:
            break
    if len(A)==6:
        print(*A)
'''


'''#6 110203,110246
for i in range(110203,110246):
    A=[]
    for j in range(1,i+1):
        if j%2==0 and i%j==0:
            A.append(j)
        if len(A)>4:
            break
    if len(A)==4:
        print(*A)'''

'''#9  84052,84131
maxdel=0
ch=0
for i in range(84052,84131):
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
    if len(A)>maxdel:
        maxdel=len(A)
        ch=i
print(maxdel,ch)'''


'''#10  120115,120201
maxdel=0
ch=0
for i in range(120115,120201):
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
    if len(A)>=maxdel:
        maxdel=len(A)
        ch=i
print(maxdel,ch)'''
'''#1 hard
for i in range(1000000,2000001):
    A=[]
    Delitel=[]
    Vtoroi_Del=[]
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            Delitel.append(j)
            Vtoroi_Del.append(int(i/j))
    for x in range(len(Delitel)):

        if abs(Delitel[x]-Vtoroi_Del[x])<=100:
            A.append(abs(Delitel[x]-Vtoroi_Del[x]))
    if len(A)>=3:
        print(i)
'''
'''#2hard
for m in range(2,33,2):
    for n in range(1,25,2):
        if ((2**m)*(3**n) >=200000000) and ((2**m)*(3**n) <=400000000):
            print((2**m)*(3**n))'''