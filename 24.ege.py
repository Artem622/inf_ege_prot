# f=open("C:/Users/Artem/Downloads/24/24.1.txt")
# a=f.read()
# f.close()
# k,maxk=0,0
# a=a.replace('КОТ','*')
# for i in a:
#     if i=='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=0
# print(maxk)

# f=open("C:/Users/Artem/Downloads/24/24.2.txt")
# a=f.read()
# f.close()
# k,maxk=0,0
# a=a.replace('AB','*')
# a=a.replace('CB','*')
# for i in a:
#     if i=='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=0
# print(maxk)

# f=open("C:/Users/Artem/Downloads/24/24.5.txt")
# a=f.readlines()
# f.close()
# maxrast=0
# for i in a:
#     if i.count('A')<25:
#         for j in range(len(i)):
#             item_0=i.find(i[j])
#             item_1 = i.rfind(i[j])
#             rast=abs(item_0-item_1)
#             maxrast=max(maxrast,rast)
# print(maxrast)

# f=open("C:/Users/Artem/Downloads/24/24.6.txt")
# a=f.read()
# f.close()
# maxcount=count=0
# a=a.replace('BOSS','*')
# for i in range(len(a)-2):
#     if a[i]!='J' and a[i+1]=='*' and a[i+2]!='J':
#         count+=1
#         maxcount=max(maxcount,count)
#
# print(maxcount)

# f=open("C:/Users/Artem/Downloads/24/24.7.txt")
# a=f.read()
# f.close()
# maxcount=count=0
# a=a.replace('RUSTEM','*')
# a=a.replace('RUS','#')
# k=0
# for i in a:
#     if i=='#':
#         k+=1
# print(k)

# f=open("C:/Users/Artem/Downloads/24/24.8.txt")
# a=f.readlines()
# f.close()
# k=0
# for i in a:
#     b=0
#     for j in range(len(i)-2):
#         if i[j]=='F'and i[j+2]=='O':
#             b+=1
#     if b>0:
#         k+=1
# print(k)

# f=open("C:/Users/Artem/Downloads/24/24.9.txt")
# a=f.read()
# f.close()
# k=0
# a=a.replace('SOCKCOS','*')
# for i in a:
#     if i=='*':
#         k+=1
# print(k)

# # A, B, C, D, E, F
# f=open("C:/Users/Artem/Downloads/24/24.10.txt")
# a=f.read()
# f.close()
# maxk=0
# a=a.replace('A','*')
# a=a.replace('E','*')
# a=a.replace('B','#')
# a=a.replace('C','#')
# a=a.replace('D','#')
# a=a.replace('F','#')
# k=0
# for i in a:
#     if i=='#':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=0
# print(maxk)

# f=open("C:/Users/Artem/Downloads/24/24.11.txt")
# a=f.read()
# f.close()
# simv=[0]*50
# for i in range(len(a)-1):
#     if a[i]=='X':
#         simv[ord(a[i+1])-65]+=1
# ind=max(simv)
# inde = simv.index(ind)
# print(chr(inde+65),ind)

# f=open("C:/Users/Artem/Downloads/24/24.12.txt")
# a=f.read()
# f.close()
# a=a.replace('A','*')
# a=a.replace('E','*')
# k=maxk=0
# for i in a:
#     if i!='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=0
# print(maxk)

# f=open("C:/Users/Artem/Downloads/24/24.13.txt")
# a=f.read()
# f.close()
# a=a.replace('abc','#')
# k=0
# print(a.count('#'))


# f=open("C:/Users/Artem/Downloads/24/24.14.txt")
# el=f.read()
# f.close()
# e=[0]*50
# for i in range(len(el)-2):
#     if el[i+1]==el[i+2]:
#         e[ord(el[i])-65]+=1
# ind = max(e)
# inde = e.index(ind)
# print(chr(inde+65),ind)

# f=open("C:/Users/Artem/Downloads/24/24.15.txt")
# a=f.read()
# f.close()
# k=0
# maxk=0
# for i in a:
#     if i!='G' and i!='W' and i!='P':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=0
# print(maxk)

# f=open(("C:/Users/Artem/Downloads/24/24.16.txt"))
# a=f.readlines()
# f.close()
# maxrast=0
# for i in a:
#     if i.count('A')<25:
#         for j in range(len(i)):
#             k1=i.find(i[j])
#             k2=i.rfind((i[j]))
#             rast=abs(k1-k2)
#             maxrast=max(maxrast,rast)
# print(maxrast)

# f=open("C:/Users/Artem/Downloads/24/24.17.txt")
# a=f.read()
# f.close()
# maxk=0
# k=0
# a=a.replace('XYZ','XY YZ')
# print(len(max(a.split(),key=len)))

# f=open("C:/Users/Artem/Downloads/24/24.18.txt")
# a=f.read()
# f.close()
# a=a.replace('XZZY','XZZ ZZY')
# print((len(max(a.split(),key=len))))

# f = open("C:/Users/Artem/Downloads/24/24.19.txt")
# a=f.read()
# f.close()
# a=a.replace('XY','X Y')
# a=a.replace('XZ','X Z')
# m=0
# for i in a.split(' '):
#     m=max(m,len(i))
# print(m)

# f = open("C:/Users/Artem/Downloads/24/24.20.txt")
# a=f.read()
# f.close()
# maxk=k=0
# for i in range(len(a)-1):
#     if (a[i]=='a' and a[i+1]=='d') or (a[i]=='d' and a[i+1]=='a'):
#         k=1
#     else:
#         k+=1
#         maxk=max(maxk,k)
# print(maxk)

# f = open("C:/Users/Artem/Downloads/24/24.22.txt")
# a=f.read()
# f.close()
# maxk=k=0
# for i in range(len(a)-1):
#     if (a[i]=='R'and a[i+1]=='P')or(a[i]=='P'and a[i+1]=='R'):
#         k=1
#     else:
#         k+=1
#         maxk=max(maxk,k)
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.25.txt")
# a=f.read()
# f.close()
# k=maxk=0
# a=a.split('D')
# for i in range(len(a)-2):
#     x=a[i]+'D'+a[i+1]+'D'+a[i+2]
#     maxk=max(maxk,len(x))
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.26.txt")
# a=f.read()
# f.close()
# maxk=0
# a=a.split('A')
# for i in range(len(a)-1):
#     x=a[i]+'A'+a[i+1]
#     maxk=max(maxk,len(x))
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.27.txt")
# a=f.read()
# f.close()
# k=maxk=0
# for i in range(len(a)-2):
#     if not(a[i]==a[i+1] and a[i+1]==a[i+2]):
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=0
# print(maxk+2)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.28.txt")
# a=f.read()
# f.close()
# print(a.count('XVIII'))

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.29.txt")
# a=f.read()
# f.close()
# k=0
# for i in range(len(a)-3):
#     if a[i]=='X'and a[i+1]=='X' and a[i+2]=='X' and a[i+3]=='X':
#         k+=1
# print(k)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.31.txt")
# i=f.read()
# f.close()
# k=0
# for j in range(len(i)-3):
#     if i[j]=='G' and i[j+2]=='M' and i[j+3]=='E':
#         k+=1
# print(k)

# import collections
# f=open("C:\\Users\\Artem\\Downloads\\24\\24.32.txt")
# a=f.read()
# f.close()
# print(collections.Counter(a).most_common())

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.33.txt")
# a=f.read()
# f.close()
# k,maxk=0,0
# kt=0
# ky=0
# for i in a:
#     if ky<1 and kt<=5:
#         if i=='Y':
#             ky=1
#         if i=='.':
#             kt+=1
#         k+=1
#         maxk=max(k,maxk)
#     else:
#         k=0
#         kt=0
#         ky=0
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.34.txt")
# a=f.read()
# f.close()
# a=a.replace('ZX','*')
# a=a.replace('ZY','*')
# maxk=0
# k=0
# for i in range(len(a)-1):
#     if a[i]=='*' and a[i+1]=='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=1
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.35.txt")
# a=f.read()
# f.close()
# maxk,k=0,0
# a=a.replace('ZXY','*')
# a=a.replace('ZYX','*')
# for i in range(len(a)-1):
#     if a[i]=='*' and a[i+1]=='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:k=1
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.36.txt")
# a=f.read()
# f.close()
# a=a.replace('AA','*')
# a=a.replace('CC','*')
# maxk,k=0,0
# for i in range(len(a)-1):
#     if a[i]=='*' and a[i+1]=='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=1
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.40.txt")
# a=f.readlines()
# f.close()
# #195.2?.1?5.14,
# k=0
# for i in a:
#     if i[0]=='1' and i[1]=='9' and i[2]=='5' and i[3]=='.' and i[4]=='2' and i[6]=='.' and i[7]=='1' and i[9]=='5' and i[10]=='.' and i[11]=='1'and i[12]=='4':
#         k+=1
# print(k)

# f=open("C:\\Users\\Artem\\Downloads\\24 (6).txt")
# a=f.read()
# f.close()
# maxk,k=0,0
# for j in range(2):
#     for i in range(j,len(a)-1,2):
#         if a[i]+a[i+1]=='AA' or a[i]+a[i+1]=='CC':
#             k+=1
#             maxk=max(maxk,k)
#         else:
#             k=0
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.51.txt")
# a=f.read()
# f.close()
# m1 = max(a.replace('PR','P R').split(),key=len)
# m2 = max(a.replace('ST','S T').split(),key=len)
# print(max(len(m1),len(m2)))

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.53.txt")
# a=f.read()
# f.close()
# a=a.replace('C',' ')
# a=a.replace('F',' ')
# m=0
# for i in a.split(' '):
#     m=max(m,len(i))
# print(m)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.55.txt")
# a=f.read()
# f.close()
# a=a.replace('A',' ')
# a=a.replace('E',' ')
# m=0
# for i in a.split(' '):
#     m=max(m,len(i))
# print(m)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.57.txt")
# a=f.read()
# f.close()
# print(a.count('abc'))

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.58.txt")
# a=f.read()
# f.close()
# a=a.replace('G',' ')
# a=a.replace('W',' ')
# a=a.replace('P',' ')
# m=0
# for i in a.split(' '):
#     m=max(m,len(i))
# print(m)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.59.txt")
# a=f.read()
# f.close()
# a=a.replace('W',' ')
# a=a.replace('R',' ')
# a=a.replace('Q',' ')
# m=0
# for i in a.split(' '):
#     m = max(m,len(i))
# print(m)

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.60.txt")
# a=f.read()
# f.close()
# a=a.replace('XZZY','XZZ ZZY')
# print(len(max(a.split(),key=len)))

# f=open("C:\\Users\\Artem\\Downloads\\24\\24.20.txt")
# a=f.read()
# f.close()
# k,maxk=0,0
# for i in range(len(a)-1):
#     if (a[i]=='a' and a[i+1]=='d') or (a[i]=='d' and a[i+1]=='a'):
#         k=1
#
#     else:
#         k+=1
#         maxk = max(maxk, k)
# print(maxk)

import random

print(random.randint(0,180))