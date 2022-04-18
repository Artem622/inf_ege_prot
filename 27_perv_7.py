'''
#27424
f=open("C:\\Users\\Artem\\Downloads\\27.1.B.txt")
sum=0
minr=100000000000
n=f.readline()
for line in f.readlines():
    a=int(line.split()[0])
    b=int(line.split()[1])
    sum += max(a,b)
    if abs(a-b)>0 and abs(a-b)<minr and abs(a-b)%3!=0:
        minr=abs(a-b)
if sum%3!=0:
    print(sum)
else:
    print(sum-minr)'''

'''
#27889
f=open("C:\\Users\\Artem\\Downloads\\27.2.B.txt")
sum=0
minr=100000000000
n=f.readline()
for i in f.readlines():
    a=int(i.split()[0])
    b=int(i.split()[1])
    sum+=min(a,b)
    if abs(a-b)<minr and abs(a-b)>0 and abs(a-b)%3!=0:
        minr=abs(a-b)
if sum%3!=0:
    print(sum)
else:
    print((sum-minr))
'''

'''
#27890
f=open("C:\\Users\\Artem\\Downloads\\27.3.B.txt")
sum=0
minr=100000000000
n=f.readline()
for i in f.readlines():
    a=int(i.split()[0])
    b=int(i.split()[1])
    sum+=max(a,b)
    if abs(a-b)<minr and abs(a-b)>0 and abs(a-b)%5!=0:
        minr=abs(a-b)
if sum%5!=0:
    print(sum)
else:
    print((sum-minr))
'''

'''
#27891
n,*data=open("C:\\Users\\Artem\\Downloads\\27.4.B.txt").read().split()
n=int(n)
data=list(map(int,data))
all_ch=set(data)
all_chh=[]
for i in all_ch:
    all_chh.append(i)
maxx=0
for i in range(len(all_chh)):
    for j in range(i+1,len(all_chh)):
        if all_chh[i]*all_chh[j]%14==0:
            maxx=max(maxx,all_chh[i]*all_chh[j])
print(maxx)

'''

'''
#27985
n,*data=open("C:\\Users\\Artem\\Downloads\\27.5.A.txt").read().split()
n=int(n)
data=list(map(int,data))
all_ch=set(data)
all_chh=[]
for i in all_ch:
    all_chh.append(i)
maxx=0
for i in range(len(all_chh)):
    for j in range(i+1,len(all_chh)):
        if all_chh[i]*all_chh[j]%14==0:
            maxx=max(maxx,all_chh[i]*all_chh[j])
print(maxx)
'''

'''
#27986
data=open("C:\\Users\\Artem\\Downloads\\27.6.B.txt").read().split()
data=list(map(int,data))
data.pop(-1)
all_ch=set(data)
all_chh=[]
for i in all_ch:
    all_chh.append(i)
maxx=0
for i in range(len(all_chh)):
    for j in range(i+1,len(all_chh)):
        if all_chh[i]*all_chh[j]%7==0 and all_chh[i]*all_chh[j]%49!=0:
            maxx=max(maxx,all_chh[i]*all_chh[j])
print(maxx)
'''

'''
#27988
n,*data=open("C:\\Users\\Artem\\Downloads\\27.7.B.txt").read().split()
data=list(map(int,data))
all_ch=set(data)
all_chh=[]
for i in all_ch:
    all_chh.append(i)
maxx=0
for i in range(len(all_chh)):
    for j in range(i+1,len(all_chh)):
        if all_chh[i]*all_chh[j]%26==0 :
            maxx=max(maxx,all_chh[i]*all_chh[j])
print(maxx)
'''