# f=open("C:\\Users\\Artem\\Downloads\\10 Собачье сердце.txt")
# a=f.read()
# f.close()
# k=0
# for i in a.split():
#     if (i.count('в')>0 or i.count('В')>0) and i.count('а')==0 and i.count('о')==0 and i.count('О')==0 and i.count('А')==0:
#         k+=1
# print(k)

# def f(n):
#     k=0
#     while n>1:
#         k=k+1
#         if n%6==0:
#             n=n//6
#     if k<4:
#         return k
#     else:
#         return (k%4)
#
# for n in range(10000,1,-1):
#     if n==6 or n==36 or n==36*6 or n==36*36 or n==36*36*6 or n==36*36*36:
#         print(f(n),n)
# import math
# #Del=[]
# def isprime(x):
#     d=2
#     while d*d<=x:
#         if x%d==0:
#             return False
#         d+=1
#     return True
#
# for i in range(960001,10000000):
#     Del=[]
#     for j in range(2,i//2+1):
#         if i%j==0 and isprime(j)==1 and j%10==3:
#             Del.append(j)
#     if len(Del)>=3:
#         print(i,sum(Del))
# # for i in range(1000000):
#     if i%10==3 and isprime(i)==1:
#         Del.append(i)
# print(Del)
# for i in range(960001,10000000):
#     kp=0
#     s=0
#     for j in Del:
#         if i%j==0:
#             kp+=1
#             s+=j
#     if kp>=3:
#         print(i,s)


# A=0
# t=[]
# while True:
#     for x in range(0,1000):
#         for y in range(0,1000):
#             if not(((x>8) <=(x*x+3*x>=A))and((y*y+5*y>A)<=(y>=4))):
#                 break
#         else:
#             continue
#         break
#     else:
#         t.append(A)
#         print(len(t))
#     A+=1

f=open("C:\\Users\\Artem\\Downloads\\24.es.txt")
a=f.read()
f.close()
a=a.split('A')
maxk=0
for i in range(len(a)-3):
    s=a[i]+'A'+a[i+1]+'A'+a[i+2]+'A'+a[i+3]
    if s.count('R')==0:
        maxk=max(maxk,len(s))
print(maxk)