'''#1
f=open("C:\\Users\\Artem\\Downloads\\27.1.B.txt")
sum=0
minr=1000000000000000000000
n=f.readline()
for line in f.readlines():
    a=int(line.split()[0])
    b=int(line.split()[1])
    sum+=max(a,b)
    if abs(a-b)>0 and abs(a-b)<minr and abs(a-b)%3!=0:
        minr=abs(a-b)
if sum%3!=0:
    print(sum)
else:
    print(sum-minr)'''

'''#2
f=open("C:\\Users\\Artem\\Downloads\\27.2.B.txt")
sum=0
minr=1000000000000000000000
n=f.readline()
for line in f.readlines():
    a=int(line.split()[0])
    b=int(line.split()[1])
    sum+=min(a,b)
    if abs(a-b)>0 and abs(a-b)<minr and abs(a-b)%3!=0:
        minr=abs(a-b)
if sum%3!=0:
    print(sum)
else:
    print(sum-minr)'''

'''#3
f=open("C:\\Users\\Artem\\Downloads\\27.3.B.txt")
sum=0
minr=1000000000000000000000
n=f.readline()
for line in f.readlines():
    a=int(line.split()[0])
    b=int(line.split()[1])
    sum+=max(a,b)
    if abs(a-b)>0 and abs(a-b)<minr and abs(a-b)%5!=0:
        minr=abs(a-b)
if sum%5!=0:
    print(sum)
else:
    print(sum-minr)'''

'''
#4
n,*data=open("C:\\Users\\Artem\\Downloads\\27.4.B.txt").read().split()
n=int(n)
data=list(map(int,data))
vse=set(data)
vseh=[]
for i in vse:
    vseh.append(i)
maxx=0
for i in range(len(vseh)):
    for j in range(i+1,len(vseh)):
        if vseh[i]*vseh[j]%14==0:
            maxx = max(maxx, vseh[i] * vseh[j])
print(maxx)
'''