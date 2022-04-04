'''f=open("C:/Users/Artem/Downloads/test24.txt")
s=f.readline()
f.close()
k=1
maxlen=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        k+=1
        maxlen=max(maxlen,k)
    else:
        k=1
print(maxlen)'''



'''f=open("C:/Users/Artem/Downloads/test24.2.txt")
s=f.readline()
f.close()
k=0
maxk=0
for i in range(len(s)-1):
    if s[i]=='X':
        k+=1
        maxk=max(maxk,k)
    else:
        k=0
print(maxk)'''



'''f=open("C:/Users/Artem/Downloads/test24.3.txt")
s=f.readline()
f.close()
count=0
maxcount=0
for i in range(len(s)-1):
    if (s[i]=='X' and count%3==0) or (s[i]=='Y' and count%3==1) or (s[i]=='Z' and count%3==2):
        count+=1
        maxcount=max(count,maxcount)
    elif s[i]=='X':
        count=1
    else:
        count=0
print(maxcount)'''



'''countSTR=0
with open("C:/Users/Artem/Downloads/222444.txt") as f:
    for a in f.readlines():
        if a.count('A')>a.count('E'):
            countSTR+=1
print(countSTR)
'''


'''import collections
f=open("C:/Users/Artem/Downloads/trtr.txt")
a=f.readlines()
f.close()
s='N'*100000000
for i in a:
    if i.count('N')<s.count('N'):
        s=i
print(collections.Counter(s).most_common(1))'''

'''f=open("C:/Users/Artem/Downloads/prom.txt")
a=f.readline()
f.close()
A=[0]*50
for i in range(len(a)):
    if a[i]=='A' and a[i+1]!='A':
        A[ord(a[i+1])-65]+=1
ind=max(A)
index=A.index(ind)
print(chr((index+65)))
'''


#HArd_ThE_First
'''f=open("C:/Users/Artem/Downloads/hard.txt")
a=f.readlines()
f.close()
maxrast=0
for i in a:
    if i.count('A')<25:
        for j in range(len(i)):
            item_0=i.find(i[j])
            item_1 = i.rfind(i[j])
            rast=abs(item_0-item_1)
            maxrast=max(maxrast,rast)
print(maxrast)

'''
'''
f=open('_')
s=f.read()
a=s.split('B')
mx=-1
for i in a:
    if i.count('A')>=3:
        mx=max(len(i),mx)
print(mx)
'''
'''f=open("C:/Users/Artem/Downloads/rep.txt")
a=f.readlines()
f.close()
k=0
for i in a:
    if i.count('E')>i.count('A'):
        k+=1
print(k)'''

'''f=open("C:/Users/Artem/Downloads/rep2.txt")
a=f.read()
f.close()
A=[0]*50
for i in range(len(a)-1):
    if a[i]=='E':
        A[ord(a[i+1])-65]+=1
index=A.index(max(A))
print(chr(index+65))'''

'''with open("C:/Users/Artem/Downloads/rep4.txt")as f:
    s = f.read()
    s = s.replace('XZZY','AAA AAA')
print(len(max(s.split(),key=len)))'''

'''import re

a=open("C:/Users/Artem/Downloads/rep5.txt")
s = a.read()
a.close()
print(max(map(len, re.split('(?<=K)(?=L)|(?<=L)(?=K)', s))))'''

f=open('24.txt')
s=f.read()
f.close()
count=1
mx=0
for i in range(len(s)-1):
    if s[i]=='P' and s[i+1]=='P':
        count=1
    else:
        count=count+1
        mx = max(mx, count)
print(mx)