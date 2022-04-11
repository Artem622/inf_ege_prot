'''
№1(standart sisadmin)
s,n,*data=open('C:/Users/Artem/Downloads/26.3.txt').read().split()
s,n=int(s),int(n)
data=sorted(map(int,data))
for i in range(len(data)):
    if s-data[i]>=0:
        s= s-data[i]
    else:
        print(i, data[i-1:])
        break
print(s)

'''



'''
#MAGAZIN
from math import ceil
n,*data=open('C:/Users/Artem/Downloads/26.test.txt').read().split()
n=int(n)
data=list(map(int,data))

sump=0
maxc=0
A=[]
for i in range(len(data)):
    if data[i]<=50:
        sump+=data[i]
    else:
        A.append(data[i])
A=sorted(A)
for i in range(len(A)):
    if i < len(A)//2:
        sump += A[i]*0.75
        maxc = A[i]
    else:
        sump += A[i]
sump=ceil(sump)
print(sump, maxc)'''



'''#грузовик с ошибкой, проклятое решение елки-палки


n,m,*data=open("C:/Users/Artem/Downloads/26.19.txt").read().split()
n,m=int(n),int(m)
data=sorted(map(int,data))
Vsegr=[]
Perv=[]
for i in data:
    if 210<=i<=220:
        Perv.append(i)
    else:
        Vsegr.append(i)
k_per=len(Perv)
s_per=sum(Perv)
n-=k_per
m-=s_per
kolicestvo=0
summa=0
for i in range(len(Vsegr)):
    if m-Vsegr[i]>=0:
        summa+=Vsegr[i]
        kolicestvo+=1
        m= m-Vsegr[i]
    else:
        print(i, Vsegr[i-1:])
        break
print(m,'свободное место')
print(summa+s_per,'общий вес')
print(kolicestvo+k_per,'количество грузов' )
print((Vsegr))'''

'''
#грузовик абсолютно верно)))

n,m,*data=open("C:/Users/Artem/Downloads/26.19.txt").read().split()
n,m=int(n),int(m)
data=sorted(map(int,data))
W_perv=[]
W_ost=[]
for i in data:
    if 210 <= i <= 220:
        W_perv.append(i)
    else:
        W_ost.append(i)
W_tek=[]
m-=sum(W_perv)
for i in range(len(W_ost)):
    if sum(W_tek)+W_ost[i]<=m:
        W_tek.append(W_ost[i])
j=1
while j<len(W_tek):
    maxI=m-sum(W_tek)+W_tek[-j]
    while not(maxI in W_ost):
        maxI-=1
    W_tek[-j]=maxI
    j+=1
count=len(W_tek)+len(W_perv)
zagr=sum((W_tek))+sum((W_perv))
print(count,zagr)'''

'''
предприятия 20

f=open("C:/Users/Artem/Downloads/26.20.txt")
N,M=map(int,f.readline().split())
A=[]
ksum,count_B=0,0
for i in range(N):
    x,y,z=f.readline().split()
    A.append((z,int(x),int(y)))
A.sort( key=lambda i:((i[0]),i[1]) )
for k in A:
    if ksum+k[1]>M:
        break
    for i in range(k[2]):
        if ksum+k[1]<=M:
            ksum+=k[1]
            if k[0]=='B':
                count_B+=1
print(count_B,M-ksum)'''

'''
предприятия 21
f=open("C:/Users/Artem/Downloads/26.20.txt")
N,M=map(int,f.readline().split())
A=[]
ksum,count_B=0,0
for i in range(N):
    x,y,z=f.readline().split()
    if z=='A':
        z='B'
    else:
        z='A'
    A.append((z,int(x),int(y)))
A.sort( key=lambda i:((i[0]),i[1]) )
for k in A:
    if ksum+k[1]>M:
        break
    for i in range(k[2]):
        if ksum+k[1]<=M:
            ksum+=k[1]
            if k[0]=='B':
                count_B+=1
print(count_B,M-ksum)'''

'''
среднее арифметическое 22


N,*data=open("C:/Users/Artem/Downloads/26.22.txt").read().split()
N=int(N)
data=list(map(int,data))
Vse=set(data)
Chet=[]
maxsr=0
count=0
for i in data:
    if i%2==0:
        Chet.append(i)
for i in range(len(Chet)):
    for j in range(i-1):
        if (Chet[i]+Chet[j])//2 in Vse:
            count+=1
            maxsr=max(maxsr, (Chet[i]+Chet[j])//2)
print(count,maxsr)

'''
'''

херота 28 и 29 я ебал
f=open("C:/Users/Artem/Downloads/26.29.txt")
N,M=map(int,f.readline().split())
data=[]
for i in range(N):
    ch,par=f.readline().split()
    data.append((int(ch),par))
data.sort()

count, S = {}, 0
for i in range(N):
  v, m = data[i]
  if S+v <= M:
    iLast = i
    S += v
    count[m] = count.get(m, 0) + 1

remaining = [ (v, m) for v, m in data[iLast+1:]
                        if m == 'B']

i = iLast
while remaining and i >= 0:
  v, m = data[i]
  if m != 'B':
    vA, mA = remaining.pop(0)
    if S - v + vA <= M:
      count['B'] = count.get('B', 0) + 1
      S = S - v + vA
    else:
      break
  i -= 1

print( count['B'], M - S  )
'''

'''
24
N,*data=open("C:/Users/Artem/Downloads/26.24.txt").read().split()
N=int(N)
data=list(map(int,data))
Vse=set(data)
Chet=[]
maxsr=0
count=0
for i in range(N):
    for j in range(i-1):
        if (data[i]%2==0 and data[j]%2==1) or (data[i]%2==1 and data[j]%2==0):
            a=data[i]+data[j]
            if a in Vse:
                count+=1
                maxsr=max(maxsr, a)
print(count,maxsr)'''
'''
26.27
f=open("C:/Users/Artem/Downloads/26.27.txt")
N=int(f.readline())
A=[]
for i in range(N):
    x,y=f.readline().split()
    A.append((int(x),int(y)))
A.sort( key=lambda i:(-(i[0]),(i[1])))
for i in range(len(A)-1):
    if A[i+1][1]-A[i][1]==3:
        print(A[i][0],A[i][1]+1)
        break
'''
f=open("C:/Users/Artem/Downloads/26.30.1.txt")
n=int(f.readline())
tl=[]
for i in range(n):
    st,end=map(int,f.readline().split())
    if end==0: end=17000000000
    tl.append((st,1))
    tl.append((end,-1))
    # добавим нач и кон недели
tl.append((1634515200,0))
tl.append((1634515200+7*24*60*60,-1))
tl.sort()
l,ml,mt=0,0,0
for i in range(2*n):
    t,k=tl[i]
    l+=k
    if 1634515200<=t<=1634515200+7*24*60*60:
        if l>ml:
            ml,mt=l,0
        if l==ml:
            mt+=tl[i+1][0]-t
print(ml,mt)
'''
#сумма одинаковой четности и в файле
N,*data=open("C:\\Users\\Artem\\Downloads\\no6.txt").readlines()
N=int(N)
data=list(map(int,data))
vse=set(data)
k=0
maxx=0
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i] %2== data[j]%2 and ((data[i]+data[j]) in vse):
            k+=1
            maxx=max(maxx,data[i]+data[j])
print(k,maxx)

'''