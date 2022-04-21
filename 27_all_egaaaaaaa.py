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

'''
#27989
n,*data=open("C:\\Users\\Artem\\Downloads\\27.8.B.txt")
n=int(n)
data=list(map(int,data))
a26=[]
a13=[]
a2=[]
ost=[]
for i in data:
    if i%26==0:
        a26.append(i)
    elif i%13==0:
        a13.append(i)
    elif i%2==0:
        a2.append(i)
    else:
        ost.append(i)
k=len(a26)*((len(a26)-1)//2+len(a13)+len(a2)+len(ost))+len(a13)*len(a2)
print(k)
'''

'''
#27991
n,*data=open("C:\\Users\\Artem\\Downloads\\27.10.A.txt").read().split()
data=list(map(int,data))
maxx=0
a17_1=[0]#кратные 17 и нечетные
a17_2=[0]#кратные 17 и четные
a_1=[0]#некратные 17 и нечетные
a_2=[0]#некратные 17 и четные
for i in data:
    if i %17==0 and i%2==0:
        a17_2.append(i)
    elif i%17==0 and i%2==1:
        a17_1.append(i)
    elif i%17!=0 and i%2==0:
        a_2.append(i)
    elif i%17!=0 and i%2==1:
        a_1.append(i)
a17_1.sort()
a17_2.sort()
a_1.sort()
a_2.sort()
a=max(a17_2)
b=max(a_2)
c=max(a17_1)
d=max(a_1)
if a+b>c+d:
    print(max(a,b),min(a,b))
else:
    print(max(c,d),min(c,d))
'''

'''
#28128
n,*data=open("C:\\Users\\Artem\\Downloads\\27.11.B.txt").read().split()
n=int(n)
data=list(map(int,data))
all_ch=set(data)
all_chh=[]
for i in all_ch:
    all_chh.append(i)
maxx=1
for i in range(len(all_chh)):
    for j in range(i+1,len(all_chh)):
        if (all_chh[i]+all_chh[j])%3==0:
            maxx=max(maxx,all_chh[i]+all_chh[j])
print(maxx)

'''