'''def f(i):
    d=2
    while d**2<=i:
        if i%d==0:
            break
        d+=1
    return True

for i in range(77777777,88888889):
    x=i
    while x%2==0:
        x=x//2
    t=int(x**0.25)
    if f(t)==1 and t**4==x:
        print(i,t)'''



'''for i in range(126849,126872):
    A=[]
    for j in range(1,int(i**0.5)+1):
        if i%j==0:
            A.append(j)
            A.append((i/j))
        if len(A)>4:
            break
    if len(A) == 4:
        print(*sorted(A))'''
'''for i in range(194455,194501):
    A=[]
    for j in range(1,int(i**0.5)):
        if i%j==0:
            A.append(j)
            A.append((i/j))
        if len(A)>4:
            break
    if len(A)==4:
        print(*sorted(A))'''

'''
на 5 делителей 29
a = 652938
b = 1744328
for n in range(a, b + 1):
    A = []
    if int(n**0.5) == n**0.5:
      for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            A.append(d)
            if d != n/d:
                A.append(n/d)
            if len(A) > 3:
                break
      if len(A) ==3:
        print(1,*sorted(A),n)'''



'''
30


=904528
b=997438
for i in range(a,b+1):
    A=[]
    if int(i**0.5)==i**0.5:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                A.append(j)
                if j!=i/j:
                    A.append(i/j)
            if len(A)>3:
                break
        if len(A)==3:
            print(1,*sorted(A),i)'''


'''
на 5 блядских делителей
a=1820348
b=2880927
for i in range(a,b+1):
    A=[]
    if int(i**0.5)==i**0.5:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                A.append(j)
                if j!=i/j:
                    A.append(i/j)
            if len(A)>3:
                break
        if len(A)==3:
            print(1,*sorted(A),i)

'''

'''32

a=394441
b=394505
ch=0
chd=0
maxdel=0
for i in range(a,b+1):
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
    if len(A)>maxdel:
        maxdel=len(A)
        ch=A[-1]
        chd=A[-2]
print(maxdel,ch,chd)'''

'''
37
x=248015
y=251575
k=0
for i in range(x,y+1,2):
    ch=0
    A=[]
    for j in range(1,i+1):
        if i%j==0:
            A.append(j)
            if j**2==i:
                ch=j
    if len(A)%2==1:
        k+=1
        print(k,i,len(A),ch)
'''

'''
40
def f(i):
    d=2
    while d**2<=i:
        if i%d==0:
            return False
        d+=1
    return True

k=0
for i in range(2943444,2943530):
    if f(i)==1:
        k+=1
        print(k,i)
'''

'''
def f(i):
    d=2
    while d**2<=i:
        if i%d==0:
            return False
        d+=1
    return True

A=[]
B=[]
k=0
for i in range(3532000,3532161):
    if f(i)==1:
        k+=1
        A.append(i)
        B.append(k)
for j in range (len(A)):
    A.sort(reverse=True)
    print(B[j],A[j])

'''

'''
65
def f(n):
    d=2
    while d**2<=n:
        if n%d==0:
            return False
        d+=1
    return True

k=0

for n in range(2532000,2532161):
    if f(n)==1:
        k+=1
        if k%3==1:
            print(k,n)

'''

'''
67
a=33333
b=55555
A=[]
for i in range(a,b+1):
    r=str(i)
    c=int(r[0])
    m=int(r[1])
    z=int(r[-1])
    x=int(r[2])
    b=int(r[3])
    if i%6!=0 and i%7!=0 and i%8!=0 and z%2==0 and x%2==0 and c%2==1 and m%2==1 and b%2==1 :
        A.append(i)
print(len(A), (A[-1]-A[0]))
'''

'''
71
def prostoe(i):
    d=2
    while d**2 <=i:
        if i%d==0:
            return False
        d+=1
    return True

count=0
for i in range(2,20001):
    k = 0
    if prostoe(i)==0:
        for j in range(2,i+1):
            if i%j==0 and prostoe(j)==True:
                k+=1
    if k>3:
        count+=1
print(count)
'''

'''

sumch=0
for i in range(2945,18295):
    k=0
    for j in range(2,int(i**0.5)+1):
        if i%(j**2)==0:
            break
    else:
        sumch+=sum(map(int,str(i)))
print(sumch)'''