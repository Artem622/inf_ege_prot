# a='8'*84
# while '1111' in a or '8888' in a:
#     if '1111' in a:
#         a=a.replace('1111','8',1)
#     else:
#         a=a.replace('8888','11',1)
# print(a)

# #неизвестность по цифрам
# for a in range(1,30):
#     for b in range(1,30):
#         for c in range(1,30):
#             x='0'+'1'*a+'2'*b+'3'*c+'0'
#             while not('00') in x:
#                 x=x.replace('01','21022')
#                 x=x.replace('02','310')
#                 x=x.replace('03','230112')
#                 if x.count('1')==96 and x.count('2')==36 and x.count('3')==80:
#                     print(a+b+c+2)

# def vodka(x,a,b):
#     s=''
#     x=int(str(x),a)
#     while x>0:
#         s=s+str(x%b)
#         x=x//b
#     return s[::-1]
#
# ok=['61','62','63','64','65']
# tr=vodka(53**123+65**2222-172**12,10,7)
# k=tr.count('61')+tr.count('62')+tr.count('63')+tr.count('64')+tr.count('65')
# print(k)

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n<3:
#         return 1
#     if n>2 and sum(map(int,str(n)))%2==0:
#         return f(n-1)-f(n-2)
#     if n > 2 and sum(map(int, str(n))) % 2 == 1:
#         return f(n-1)+f(n//2)
# print(f(100))
#
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n==0:
#         return 1
#
#     return f(n-1)*n
# print(f(400000))

# def f(x,end):
#     if x==end:
#         return 1
#     if x<end:
#         return 0
#     return f(x-3,end)+f(x//2,end)
#
# print(f(108,42)*f(42,12))


# f=open("C:\\Users\\Artem\\Downloads\\24 (9).txt")
# a=f.read()
# f.close()
# maxk,k=0,0
# for j in range(2):
#     for i in range(j,len(a)-2,2):
#         if a[i]+a[i+1]+a[i+2]=='AB' or a[i]+a[i+1]+a[i+2]=='CAC':
#             k+=1
#             maxk=max(maxk,k)
#         else:
#             k=0
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\24 (9).txt")
# a=f.read()
# f.close()
# maxk,k=0,0


# for i in range(-1000,1000):
#     s=i
#     p=20
#     q=13
#     k1=0
#     k2=0
#     while s<230:
#         s=s+p
#         k1=k1+1
#
#     while s>=q:
#         s=s-q
#         k2=k2+1
#     if k1==12 and k2==18:
#         print(i)

# def f(n,m):
#     return n%m==0
#
# A=1
# while True:
#     for x in range(1,1000):
#         if not((f(x,3)<=(not(f(x,5)))) or (x+A>=90)):
#             break
#     else:
#         print(A)
#     A+=1


# p1,p2,q1,q2 = 117,158,129,180
# P=[i/10 for i in range(p1*10,p2*10+1)]
# Q=[i/10 for i in range(q1*10,q2*10+1)]
#
# def f(x,A):
#     return (x in P) <=(((x in Q) and (not(x in A)))<=(not(x in P)))
#
# A=set()
# for x in [i/10 for i in range(100000)]:
#     if not f(x,A):
#         A.add(x)
# print(sorted(A))

# P=[ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# Q=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#
# def f(x,A):
#     return ((x in A) <= (x in P)) and ((x in Q) <= (not(x in A)))
#
# A=set([i for i in range(10000)])
# for x in [i for i in range(10000)] :
#     if not f(x,A):
#         A.remove(x)
# print(sorted(A))
# print(len(sorted(A)))

# def f(n,m):
#     return n%m==0
#
# A=1
# while True:
#     for x in range(1,10000):
#         if not((f(x,3)<=(not(f(x,5)))) or (x+A>=70)):
#             break
#     else:
#         print(A)

# p1,p2,q1,q2 = 10,20,35,45
# P=[i/10 for i in range(p1*10,p2*10+1)]
# Q=[i/10 for i in range(q1*10,q2*10+1)]
#
# def f(x,A):
#     return ((not(x in P)) <= (x in Q)) and (not(x in A))
#
# A=set()
# for x in [i/10 for i in range(100000)]:
#     if f(x,A):
#         A.add(x)
# print(sorted(A))


# A=0
# while True:
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if not((x*y<2*A) or (x>=11) or (x<2*y)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)
#     A+=1

# d1,d2,c1,c2 = 12,20,31,45
# D=[i/10 for i in range(d1*10,d2*10+1)]
# C=[i/10 for i in range(c1*10,c2*10+1)]
#
# def f(x,A):
#     return  ((not(x in C)) and (not(x in D))) or (((x in D) or (x in C)) <=(x in A))
#
# A=set()
# for x in [i/10 for i in range(1000000)]:
#     if not f(x,A):
#         A.add(x)
# print(sorted(A))
# p1,p2,q1,q2 = 1,39,23,58
# P=[i/10 for i in range(p1*10,p2*10+1)]
# Q=[i/10 for i in range(q1*10,q2*10+1)]
#
# def f(x,A):
#     return ((x in P) <= (not(x in Q))) <= (not(x in A))
#
# A=set([i/10 for i in range(1000000)])
# for x in [i/10 for i in range(1000000)]:
#     if not f(x,A):
#         A.remove(x)
# print(sorted(A))

# A=1
# while True:
#     for x in range(100000):
#         if not((x & 107 == 0)<=((x & 55 !=0)<=(x & A!=0))):
#             break
#     else:
#         print(A)
#     A+=1

# A=0
# while True:
#     for x in range(1,1000):
#         for y in range(1,1000):
#             if not((x**2-10*x+16>0) or (y**2-10*y+21>0) or (x*y<2*A)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)
#     A+=1


# all=[]
# A=1
# while True:
#     for x in range(1,1000000):
#         if ((x & 17 != 0)<=((x & A!=0)<=(x&58!=0))) <= ((x & 8 ==0) and (x& A!=0)and(x&58==0)):
#             break
#     else:
#         all.append(A)
#         print(len(all))

# P=[2,4,6,8,10,12,14,16,18,20]
# Q=[3,6,9,12,15,18,21,24,27,30]
# R=[12,24,36,48,60]
#
# def f(x,A):
#     return (not(x in A)) <= (((x in P) and (x in Q))<=(x in R))
#
# A=set()
# for x in [i for i in range(1000000)]:
#     if not f(x,A):
#         A.add(x)
# A=sorted(A)
# pr=1
# for i in A:
#     pr*=i
# print(A)
# print(pr)

# def newvodka(x,base):
#     sys = '0123456'
#     s=''
#     while x>0:
#         s = sys[x%base]+s
#         x=x//base
#     return s
#
# print((newvodka(49**7+7**21-7,7)).count('6'))


# def newvodka(x,base):
#     sys = '01234567'
#     s=''
#     while x>0:
#         s=sys[x%base]+s
#         x=x//base
#     return s
#
# print((newvodka(64**30+2**300-4,8)).count('7'))

# def newvodka(x,base):
#     sys = '01234567'
#     s=''
#     while x>0:
#         s=sys[x%base]+s
#         x=x//base
#     return s
#
# print((newvodka(7*512**1912+6*64**1954-5*8**1991-4*8**1980-2022,8)).count('7'))

# def newvodka(x,base):
#     sys = '0123456789ABC'
#     s=''
#     while x>0:
#         s=sys[x%base]+s
#         x=x//base
#     return s
#
# print((newvodka(2197**50-169**35-26,13)).count('C'))


# def newvodka(x,base):
#     sys= '01234'
#     s=''
#     while x>0:
#         s= sys[x%base]+s
#         x=x//base
#     return s
#
# print(sum(map(int,(newvodka(7*5**1984-6*25**777+5*125**333-4,5)))))

# def f(n):
#     if n ==0:
#         return 5
#     if n>0:
#         return 3*f(n-4)
#     if n<0:
#         return f(n+3)
#
# print(f(43))

# def f(n):
#     if n<50:
#         return n
#     if n>49:
#         return 2*g(50-n//2)
#
# def g(n):
#     if n>40:
#         return 10
#     if n<41:
#         return 30+f(n+600//n)
#
# print(f(80))

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n<3:
#         return 1
#     if n>2 and sum(map(int,str(n)))%2==0:
#         return f(n-1)-f(n-2)
#     if n>2 and sum(map(int,str(n)))%2==1:
#         return f(n-1)+f(n//2)
#
# print(f(100))

# def newvodka(x,base):
#     sys= '01234'
#     s=''
#     while x>0:
#         s= sys[x%base]+s
#         x=x//base
#     return s
#
#
# print(newvodka(12344321,5))
# print(int('12344321',5))
# #print(sum(map(int,(newvodka(7*5**1984-6*25**777+5*125**333-4,5)))))


# from functools import lru_cache
# @lru_cache(None)

# def f(n):
#     if n<3:
#         return 1
#     if n>2 and n%2==0:
#         return g(n)+f(n-1)
#     if n>2 and n%2==1:
#         return f(n-2)-2*g(n+1)
#
# def g(n):
#     if n<3:
#         return 1
#     if n>2 and n%2==0:
#         return f(n-3)+f(n-2)
#     if n>2 and n%2==1:
#         return f(n+1)-g(n-1)
#
# print(g(120))

# f=list(map(int,open("C:\\Users\\Artem\\Downloads\\17\\17.3.txt").readlines()))
# a=set(f)
# min_kr=1000000000
# for i in a:
#     if i%6==0:
#         min_kr=min(min_kr,i)
# k,maxs=0,0
# for i in range(len(f)-1):
#     if f[i]%min_kr==0 and f[i+1]%min_kr==0:
#         k+=1
#         maxs=max(maxs,f[i]+f[i+1])
# print(k,maxs)

# a=list(map(int,open("C:\\Users\\Artem\\Downloads\\17\\17.4.txt").readlines()))
# b=[]
# for i in a:
#     i=abs(i)
#     s=str(i)
#     x=int(s[0])
#     b.append(x)
# ssss=sum(b)
# k,maxs=0,0
# for i in range(len(a)-1):
#     if a[i]*a[i+1]>ssss:
#         k+=1
#         maxs=max(maxs,a[i]+a[i+1])
# print(k,maxs)


# from functools import lru_cache
#
# def moves(s):
#     a,b=s
#     return (a+1,b),(a,b+1),(a*2,b),(a,b*2)
#
# @lru_cache(None)
# def game(s):
#     if s[0]<=1 or s[1]<=1:
#         return
#     if sum(s)>=231:
#         return 'W'
#     if any(game(m)=='W' for m in moves(s)):
#         return 'P1'
#     if all(game(m)=='P1' for m in moves(s)):
#         return 'B1'
#     if any(game(m)=='B1' for m in moves(s)):
#         return 'P2'
#     if all(game(m)=='P1' or game(m)=='P2' for m in moves(s)):
#         return 'B2'
#
# for s in range(1,214):
#     if game((17,s)) is not None:
#         print(s,game((17,s)))


# from functools import lru_cache
#
# def moves(s):
#     return s//3,s-10
#
# @lru_cache(None)
# def game(s):
#     if s<=10:
#         return 'W'
#     if any(game(m)=='W' for m in moves(s)):
#         return 'P1'
#     if any(game(m)=='P1' for m in moves(s)):
#         return 'B1'
#     if any(game(m)=='B1' for m in moves(s)):
#         return 'P2'
#     if all(game(m)=='P1' or game(m)=='P2' for m in moves(s)):
#         return 'B2'
#
# for s in range(1,1000):
#     if game(s) is not None:
#         print(s,game(s))

# for i in range(1,100000):
#     x=i
#     a=1
#     b=0
#     while x>0:
#         d = x%10
#         a*=d
#         if d>5:
#             b+=d
#         x//=10
#     if a==15120:
#         print(b)

# for i in range(10000000):
#     x=i
#     q=8
#     p=10
#     k1=0
#     k2=0
#     while x<=100:
#         k1=k1+1
#         x=x+p
#     while x>=q:
#         k2=k2+1
#         x=x-q
#     l=x+k1
#     m=x+k2
#     if l==12 and m==19:
#         print(i)

# for i in range(10000000000,1,-1):
#     s=i
#     k1=k2=0
#     while s>0:
#         d=s%10
#         if d>5:
#             s=s-1
#             k1+=1
#         else:
#             s=s//10
#             k2+=1
#     if k1+k2==58:
#         print(i)

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\24.1.txt")
# a=f.read()
# f.close()
# a=a.replace('AB','*').replace('CB','*')
# k=maxk=0
# for i in range(len(a)-1):
#     if a[i]=='*' and a[i+1]=='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=1
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\24.3.txt")
# a=f.read()
# f.close()
# a=a.replace('AC','*').replace('AB','*')
# k=maxk=0
# for i in range(len(a)-1):
#     if a[i]=='*' and a[i+1]=='*':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=1
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\24.4.txt")
# a=f.read()
# f.close()
# m1 = max(a.replace('PR','P R').split(),key = len)
# m2 = max(a.replace('ST','S T').split(),key = len)
# print((max(len(m1),len(m2))))

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\24.5.txt")
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

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\24.7.txt")
# a=f.read()
# f.close()
# k=maxk=0
# k_po=0
# k_A=0
# for i in a:
#     if i=='.':
#         k_po+=1
#     if i =='A':
#         k_A+=1
#     k+=1
#     if k_po>0:
#         k_po=0
#         k=0
#         k_A=0
#     elif k_A>=3:
#         maxk=max(maxk,k)
# print(maxk)

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\24.9.txt")
# a=f.read()
# f.close()
# a=a.replace('NEWYEAR','*')
# print(a.count('*'))

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\26.les.txt")
# n=int(f.readline())
# data=[]
#
# for i in range(n):
#     A= f.readline().split()
#     a=int(A[0])
#     b=int(A[1])
#     data.append((a,b))
# data.sort()
# data.reverse()
# maxr=[]
# mest=0
# for i in range(len(data)-1):
#     a=data[i][0]#ряд
#     b=data[i][1]#место
#     c = data[i+1][0]#ряд
#     d = data[i+1][1]#место
#     if a==c and (b-d)==14:
#         maxr=a
#         mest=d+1
#         break
#
# print(maxr)
# print(mest)

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\26.kust.txt")
# n=int(f.readline())
# data=[]
# for i in range(n):
#     A=f.readline().split()
#     a=int(A[0])
#     b=int(A[1])
#     data.append((a,b))
# min_K=10000000000
# data.sort()
# data.reverse()
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if a==c:
#         min_K=min(min_K,abs(b-d))
# print(min_K-1)
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if abs(b-d)==min_K and a==c:
#         print(a)
#         break

# a=[0]*1000
# a[21]=1
# for i in range(21,62):
#     if i%10 != 0:
#         a[i+i%10]+=a[i]
#     if i>=20:
#         a[i*(i//10)]+=a[i]
#     a[i+abs(i//10-i%10)]+=a[i]
#
# print(a[62])

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\26.les.2.txt")
# n=int(f.readline())
# data=[]
# for i in range(n):
#     A=f.readline().split()
#     a=int(A[0])
#     b=int(A[1])
#     data.append((a,b))
# data.sort()
# data.reverse()
# maxk=0
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if a==c:
#         maxk=max(maxk,abs(b-d))
# print(maxk-1)
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if abs(d-b)==maxk:
#         print(a)


# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\26.les4.txt")
# n=int(f.readline())
# data=[]
# for i in range(n):
#     A=f.readline().split()
#     a=int(A[0])
#     b=int(A[1])
#     data.append((a,b))
# maxk=0
# data.sort()
# data.reverse()
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if a==c:
#         maxk=max(maxk,abs(d-b))
# print(maxk-1)
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if abs(d-b)==maxk:
#         print(a)

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\26.lesnoi.txt")
# n=int(f.readline())
# data=[]
# for i in range(n):
#     A=f.readline().split()
#     a=int(A[0])
#     b=int(A[1])
#     data.append((a,b))
# data.sort()
# data.reverse()
#
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if a==c and abs(d-b)==12:
#         print(a)
#         print(b+1,d+1)

# f=open("C:\\Users\\Artem\\Downloads\\nadr_kege\\26.2.b.txt")
# n=int(f.readline())
# data=[]
# for i in range(n):
#     A=f.readline().split()
#     a=int(A[0])
#     b=int(A[1])
#     data.append((a,b))
# data.sort()
# data.reverse()
#
# for i in range(len(data)-1):
#     a=data[i][0]
#     b=data[i][1]
#     c=data[i+1][0]
#     d=data[i+1][1]
#     if a==c and abs(d-b)==3:
#         print(a)
#         print(b+1,d+1)

# print('a b c d')
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 if ((d and ((a or (not(c)))) <= (a and b and (not(c)))))==1:
#                     print(a,b,c,d)

# A=set()
# B=[0]*1000
# for n in range(256,1,-1):
#     binn=bin(n)[2:]
#     if n%2==1:
#         binn = '1' + binn +'00'
#     if n%2==0:
#         binn = '11' +binn + '0'
#     x=int(binn,2)
#     A.add(x)
# print(A)
# A=list(A)
# for n in range(256,1,-1):
#     binn=bin(n)[2:]
#     if n%2==1:
#         binn = '1' + binn +'00'
#     if n%2==0:
#         binn = '11' +binn + '0'
#     x=int(binn,2)
#     for i in range(len(A)):
#         if A[i]==x:
#             B[i]+=1
# print(B)
# s=0
# for i in B:
#     if i==2:
#         s+=1
# print(s)

# def f(s):
#     s=s*10
#     n=3
#     while s>0:
#         s=s-n
#         n=n*2
#     return n
#
# A=[]
# for i in range(1000000000):
#     if f(i)==768:
#         A.append(i)
#         print(len(A))

# import itertools
# a=list(itertools.product('ГЕКЭ023',repeat=4))
# k=0
# for i in a:
#     k+=1
#     s=''.join(i)
#     if (s[0]=='0' or s[0]=='2' or s[0]=='3') and s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3]:
#         print(k)


# F=open("C:\\Users\\Artem\\Downloads\\teeee.txt").read().split()
# k=0
# data=list(map(int,F))
# for i in range(0,len(data)-4,5):
#     kk=0
#     a1=data[i]
#     a2=data[i+1]
#     a3=data[i+2]
#     a4=data[i+3]
#     a5=data[i+4]
#     sr = (a1+a2+a3+a4+a5)/5
#     if a1>sr:
#         kk+=1
#     if a2>sr:
#         kk+=1
#     if a3>sr:
#         kk+=1
#     if a4>sr:
#         kk+=1
#     if a5>sr:
#         kk+=1
#     if kk>=3:
#         k+=1
# print(k)


# maxl=0
# A=set()
# for i in range(203):
#     a='1'*i+'2'+'1'*(203-i)
#     while '111' in a or '222' in a:
#         if '111' in a:
#             a=a.replace('111','22',1)
#         else:
#             a=a.replace('222','11',1)
#     maxl=max(maxl,len(a))
#     A.add(a)
# print(A)

# def newvodka(x,base):
#     sus='0123456789ABCDEF'
#     s=''
#     while x>0:
#         s=sus[x%base]+s
#         x=x//base
#     return s
#
# print(sum(map(int,(newvodka(7*5**1984-6*25**777+5*125**333-4,5)))))
#
# def f(x,A):
#     return x%A==0
#
# all=[]
# A=-1000
# while True:
#     if A==0:
#         A+=1
#     for x in range(-100000,10000):
#         if not(((f(A,25) and ((f(x,24) and f(x,75))) <= f(x,A)))):
#             break
#     else:
#         all.append(A)
#         print(len(all))
#     A+=1


# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n<3:
#         return 1
#     if n>2 and n%2==0:
#         return f(n-2)-f(n-1)
#     if n>2 and n%2==1:
#         return f(n-2)-f(n-3)
#
# print(f(50))

# f=list(map(int,open("C:\\Users\\Artem\\Downloads\\17.rrrr.txt").readlines()))
# k,maxs=0,0
# sr=sum(f)/len(f)
# for i in range(len(f)-3):
#     a=f[i]
#     b=f[i+1]
#     c=f[i+2]
#     d=f[i+3]
#     if b*c>a*d:
#         maxs=max(maxs,b+c)
#         if b>sr or c>sr:
#             k+=1
# print(maxs,k)

# from functools import lru_cache
# def moves(s):
#     return s//3,s-10
#
# @lru_cache(None)
# def game(s):
#     if s<=10:
#         return 'W'
#     if any(game(m)=='W' for m in moves(s)):
#         return 'P1'
#     if all(game(m)=='P1' for m in moves(s)):
#         return 'B1'
#     if any(game(m)=='B1' for m in moves(s)):
#         return 'P2'
#     if all(game(m)=='P1' or game(m)=='P2' for m in moves(s)):
#         return 'B2'
#
# for s in range(1,1000):
#     if game(s) is not None:
#         print(s,game(s))


# for i in range(-10000,100000):
#     s=i
#     p=20
#     q=13
#     k1=0
#     k2=0
#     while s<230:
#         s = s+p
#         k1=k1+1
#
#     while s>=q:
#         s=s-q
#         k2=k2+1
#     if k1==12 and k2==18:
#         print(i)
# k=0
# for i in range(700001,1000000000):
#     if i%13==0 and k<5:
#         x=str(i)
#         if not( (x[-4]=='0' and x[-1]=='3') or (x[-5]=='0' and x[-2]=='3') or (x[-4]=='4'and x[-1]=='2')or '1' in x):
#             k+=1
#             print(i,sum(map(int,x)))

# k=0
# for i in range(700001,1000000000):
#     if i%13==0 and k<5:
#         x=str(i)
#         if not( (x[-4]=='0' and x[-1]=='3') or (x[-5]=='0' and x[-2]=='3') or (x[-4]=='4'and x[-1]=='2')or '1' in x):
#             k+=1
#             print(i,sum(map(int,x)))

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(x<=y)) or  ((not(w)) <= (not(z))) or w)==0:
#                     print(x,y,z,w)

# for i in range(100000):
#     bini=bin(i)[2:]
#     if i%2==0:
#         bini='10' + bini +'10'
#     else:
#         bini='1'+bini+'00'
#     x=int(bini,2)
#     print(x)

# def f(s):
#     s=(s-10)//7
#     n=1
#     while s>0:
#         n=n*2
#         s=s-n
#     return n
#
# for i in range(1000000):
#     if f(i)==1024:
#         print(i)

# import itertools
#
# a=list(itertools.product('АБКЛУ',repeat = 4))
# k=0
# for i in a:
#     k+=1
#
#     s=''.join(i)
#     if s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3] and s.count('А')<=1 and s.count('Б')<=1 and s.count('К')<=1 and s.count('Л')<=1 and s.count('У')<=1  :
#         print(k,s)

# def f(s):
#     s=(s-10)//7
#     n=1
#     while s>0:
#         n=n*2
#         s=s-n
#     return n
#
# for i in range(100000000):
#     if f(i)==1024:
#         print(i)

# def newvodka(x,base):
#     sus = '0123456789ABC'
#     s=''
#     while x>0:
#         s=sus[x%base]+s
#         x=x//base
#     return s
#
# print((newvodka(2197**50-169**35-26,13)).count('C'))

# def f(n,m):
#     return n%m==0
#
# A=1
# while True:
#     for x in range(1,10000):
#         if not((((not(f(x,15))) or (not(f(x,28)))) or f(x,A)) and (A>70)):
#             break
#     else:
#         print(A)
#     A+=1

# def f(n):
#     if n==1:
#         return 1
#     if n>1 and n%2==0:
#         return n*f(n-1)
#     if n>1 and n%2==1:
#         return 1+f(n-2)
#
# print(f(84))

# a=list(map(int,open("C:\\Users\\Artem\\Downloads\\lastday1.txt").readlines()))
# k,maxs=0,1000000000
# b=set(a)
# maxk=0
# for i in b:
#     if i%11==0:
#         maxk=max(maxk,i)
# for i in range(len(a)-1):
#     if a[i]>maxk or a[i+1]>maxk:
#         k+=1
#         maxs=min(maxs,a[i]+a[i+1])
# print(k,maxs)

# from functools import lru_cache
#
# def moves(s):
#     a,b=s
#     return (a+3,b),(a,b+3),(a*2,b),(a,b*2)
#
# @lru_cache(None)
# def game(s):
#     if s[0]<=1 or s[1]<=1:return
#     if sum(s)>=300:
#         return 'W'
#     if any(game(m)=='W' for m in moves(s)):
#         return 'P1'
#     if all(game(m)=='P1' for m in moves(s)):
#         return 'B1'
#     if any(game(m)=='B1' for m in moves(s)):
#         return 'P2'
#     if any(game(m)=='P2' for m in moves(s)):
#         return 'B2'
#     if any(game(m)=='B2' for m in moves(s)):
#         return 'P3'
#     if all(game(m)=='P2' or game(m)=='P3' for m in moves(s)):
#         return 'B3'
#
# for s in range(1,280):
#     if game((20,s)) is not None:
#         print(s,game((20,s)))

# all=[]
# for i in range(-100000,100000):
#     x=i
#     a=0
#     b=0
#     while x>0:
#         a+=1
#         d=x%10
#         if d%3==0:
#             b+=d
#         x//=10
#     if a==12 and b==99:
#         all.append(i)
#         print(len(all))

# A=set()
# def f(x,count):
#     if count==7:
#         A.add(x)
#         return
#     elif count>7:
#         return
#     else:
#         return f(x+2,count+1) or f(x*2,count+1)
#
# f(1,0)
# print(A)

# f=open("C:\\Users\\Artem\\Downloads\\lastday2.txt")
# a=f.read()
# f.close()
# k,maxk=0,0
# for i in range(10):
#     for j in range(0,len(a)-1,2):
#         if a[j]+a[j+1]=='DD' or a[j]+a[j+1]=='BB':
#             k+=1
#             maxk=max(maxk,k)
#         else:
#             k=0
# print(maxk)
# if 126789%39==0:
#     print(126789,126789//39)
# for i in range(1000):
#     s='12' + str(i) +'6789'
#     s=int(s)
#     if s%39==0 and s<=10**8:
#         print(s,s//39)

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(z and (not(w)))) or ((z<=w)==(x<=y))) ==0:
#                     print(x,y,z,w)

# all=[]
# for n in range(1,100000):
#     binn=bin(n)[2:]
#     if n%2==0:
#         binn = '1' +binn+'0'
#     else:
#         binn = '11'+binn+'10'
#     x=int(binn,2)
#     ss=sum(map(int,str(x)))
#     if ss>17:
#         all.append(x)
# print(bin(sum(map(int,str((min(all))))))[2:])

# def f(x):
#     s = x
#     n=5
#     while s <110:
#         s = s+n
#         n = n+1
#     return n
#
# for i in range(100000):
#     if f(i)==15:
#         print(i)

# import itertools
#
# a=list(itertools.product('ВЕКНО',repeat = 5))
# k=0
# for i in a:
#     k+=1
#     s=''.join(i)
#     if s.count('Н')==2 and s.count('К')==2:
#         print(k,s)

# f=open("C:\\Users\\Artem\\Downloads\\BtKZGfz6u.txt")
# a=f.read().split()
# f.close()
# k=0
# a=list(map(int,a))
# for i in range(0,len(a)-2,3):
#     if a[i]==60 and a[i+1]==60 and a[i+2]==60:
#         k+=1
# print(k)

# a='2'*400
# while '8888' in a or '222' in a:
#     if '222' in a:
#         a=a.replace('222','88',1)
#     else:
#         a=a.replace('8888','22',1)
# print(a)

# def newvodka(x,base):
#     sus='01234'
#     s=''
#     while x>0:
#         s=sus[x%base]+s
#         x=x//base
#     return s
# print((newvodka(5**94+25**49-130,5)).count('4'))

# p1,p2,q1,q2 = 17,54,37,83
# P=[i/10 for i in range(p1*10,p2*10+1)]
# Q=[i/10 for i in range(q1*10,q2*10+1)]
#
# def f(x,A):
#     return (x in P)<=(((x in Q) and (not(x in A)))<=(not(x in P)))
#
# A=set()
# for x in [i/10 for i in range(1000000)]:
#     if not f(x,A):
#         A.add(x)
# print(sorted(A))

# def f(n):
#     if n<5:
#         return 1+2*n
#     if n>=5 and n%3==0:
#         return 2*(n+1)*f(n-2)
#     if n>=5 and n%3!=0:
#         return 2*n+1+f(n-1)+2*f(n-2)
#
# print(f(15))


# a=list(map(int,open("C:\\Users\\Artem\\Downloads\\lastpizda1.txt").readlines()))
# k,mins=0,10000000000000000000
# maxk=0
# for i in a:
#     if i%111==0:
#         maxk=max(maxk,i)
# for i in range(len(a)-1):
#     if (a[i]>maxk or a[i+1]>maxk) and (a[i]%10==7 or a[i+1]%10==7):
#         k+=1
#         mins=min(mins,a[i]+a[i+1])
# print(k,mins)


# from functools import lru_cache
#
# def moves(s):
#     a,b=s
#     return (a+1,b),(a,b+1),(a*2,b),(a,b*2)
#
# @lru_cache(None)
# def game(s):
#     if s[0]<=1 or s[1]<=1:
#         return
#     if sum(s)>=63:
#         return 'w'
#     if any(game(m)=='w' for m in moves(s)):
#         return 'P1'
#     if all(game(m)=='P1' for m in moves(s)):
#         return 'B1'
#     if any(game(m)=='B1' for m in moves(s)):
#         return 'P2'
#     if all(game(m)=='P1' or game(m)=='P2' for m in moves(s)):
#         return 'B2'
#
# for s in range(1,32):
#     if game((2,s)) is not None:
#         print(s,game((2,s)))


# for i in range(6,10000000):
#     x=i
#     a=3*x +23
#     b=3*x -17
#     while a!= b:
#         if a>b:
#             a-=b
#         else:
#             b-=a
#     if a==10:
#         print(i)

# def f(x,end):
#     if x==30:
#         return 0
#     if x==end:
#         return 1
#     if x>end:
#         return 0
#     return f(x+1,end)+f(x*3,end)+f(x*4,end)
#
# print(f(2,15)*f(15,100))

# f=open("C:\\Users\\Artem\\Downloads\\lastpizda2.txt")
# a=f.read()
# f.close()
# a=a.replace('PR','#').replace('RP','#')
# k,maxk=0,0
# for i in a:
#     if i!='#':
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=2
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

# for i in range(800001,1000000):
#     maxd=0
#     mind=0
#     for j in range(2,i//2+1):
#         if i%j==0:
#             mind=j
#             break
#     for j in range(i//2+1,2,-1):
#         if i%j==0:
#             maxd=j
#             break
#
#     m=maxd+mind
#     if m%138==0 and m>0:
#         print(i,m)

# f=open("C:\\Users\\Artem\\Downloads\\lastpizda3.txt")
# n=int(f.readline())
# data=[]
# for i in range(n):
#     A=f.readline().split()
#     a=int(A[0])
#     b=int(A[1])
#     data.append((a,b))
# data.sort()
# data.reverse()
# print(data)
# maxk=0
# k=0
# for i in range(len(data)-1):
#     if data[i][0]==data[i+1][0] and abs(data[i][1]-data[i+1][1])==1:
#         k+=1
#         maxk=max(maxk,k)
#     else:
#         k=1
# print(maxk)
# for i in range(len(data)-1):
#     if data[i][0]==data[i+1][0] and abs(data[i][1]-data[i+1][1])==1:
#         k+=1
#     else:
#         k = 1
#     if k==14:
#             print(data[i][0])

# f=open("C:\\Users\\Artem\\Downloads\\27-B (1).txt")
# n=int(f.readline())
# data=f.readlines()
# data=list(map(int,data))
# c=0
# for i in range(n):
#     s=0
#     for x in data[i:i+20]:
#         s+=x
#         if s%39==0:
#             c+=1
# print(c)

#1?3?5?6?8

# dell=[]
# for i in range(100):
#     x=str(i)
#     if x[-1]=='2' and len(x)==2:
#         dell.append(i)
#
# for x in range(10):
#     for y in range(10):
#         for z in range(10):
#             for h in range(10):
#                 s='1'+str(x)+'3'+str(y)+'5'+str(z)+'6'+str(h)+'8'
#                 s=int(s)
#                 k_d=0
#                 del_c=[]
#                 for i in dell:
#                     if s%i==0:
#                         k_d+=1
#                         del_c.append(i)
#                         if k_d>=len(dell)/2:
#                             print(s,s//min(del_c))


# for i in range(10):
#     s='123567'+str(i)
#     s=int(s)
#     if s%169==0:
#         print(s,s//169)
#
# for i in range(1000):
#     for j in range(10):
#         s='123' + str(i) +'567'+ str(j)
#         s=int(s)
#         if s<=10**9 and s%169==0:
#             print(s,s//169)


# k=0
# for i in range(700001,1000000000):
#     if i%13==0 and k<5:
#         x=str(i)
#         if not( (x[-4]=='0' and x[-1]=='3') or (x[-5]=='0' and x[-2]=='3') or (x[-4]=='4'and x[-1]=='2')or '1' in x):
#             k+=1
#             print(i,sum(map(int,x)))

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (z or ((w or (not(y))) == (x<=z))) ==0:
#                     print(x,y,z,w)


# for i in range(1,100000):
#     bini=bin(i)[2:]
#     s=sum(map(int,bini))
#     bini = bini+str(s%2)
#     s = sum(map(int, bini))
#     bini = bini + str(s % 2)
#     x=int(bini,2)
#     if x>452:
#         print(x)

# def f(x):
#     s=x
#     n=1
#     while s>=5:
#         s=s-15
#         n=n*2
#     return n
#
# for i in range(1000000):
#     if f(i)==2048:
#         print(i)

# import itertools
#
# a=list(itertools.product('ЛЕГКО',repeat=6))
# k=0
# for i in a:
#     s=''.join(i)
#     if s.count('О')<=1 and  s[0]!='Г' and s[-1]!='Е' and s[-1]!='О':
#         k+=1
# print(k)

# a='1'+'0'*105
# while '1' in a:
#     if '100' in a:
#         a=a.replace('100','0001',1)
#     else:
#         a=a.replace('1','00',1)
# print(a.count('0'))

# A=5300
# while True:
#     for x in range(1000):
#         for y in range(1000):
#             if not((x*y>A) or (x>y) or(74>x)):
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)
#     A+=1


# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n<=2:
#         return 2
#     if n>2:
#         return f(n-1)-2*f(n-2)
#
# print(f(37))

# a=list(map(int,open("C:\\Users\\Artem\\Downloads\\17_std.txt").readlines()))
# maxk=0
# for i in a:
#     if i%22==0:
#         maxk=max(maxk,i)
# k,mins=0,10000000000000
# for i in range(len(a)-1):
#     if a[i]>maxk or a[i+1]>maxk:
#         k+=1
#         mins=min(mins,a[i]+a[i+1])
# print(k,mins)

# from functools import lru_cache
# #
# # def moves(s):
# #     a,b=s
# #     return (a+1,b),(a,b+1),(a+2,b),(a,b+2),(a+b,b),(a,b+a)
# #
# # @lru_cache(None)
# # def game(s):
# #     if s[0]<=1 or s[1]<=1:
# #         return
# #     if sum(s)>=150:
# #         return 'w'
# #     if any(game(m)=='w' for m in moves(s)):
# #         return 'p1'
# #     if all(game(m)=='p1' for m in moves(s)):
# #         return 'b1'
# #     if any(game(m)=='b1' for m in moves(s)):
# #         return 'p2'
# #     if all(game(m)=='p1' or game(m)=='p2' for m in moves(s)):
# #         return 'b2'
# #
# # for s in range(1,89):
# #     if game((61,s)) is not  None:
# #         print(s,game((61,s)))

# for i in range(-100000,100000):
#     x=i
#     l=0
#     m=0
#     while x>0:
#         m=m+1
#         if x%2 !=0:
#             l=l+1
#         x=x//2
#     if l==7 and m==8:
#         print(i)

# def f(x,end):
#     if x<end:
#         return 0
#     if x==end:
#         return 1
#     return f(x-2,end)+f(x-5,end)
# print(f(24,3))

# f=open("C:\\Users\\Artem\\Downloads\\24_std.txt")
# a=f.read()
# f.close()
# k,maxk=0,0
# kr=0
# ka=0
# for i in a:
#     if i == 'R':
#         kr+=1
#     if i=='A':
#         ka+=1
#     k+=1
#     if ka<=3 and kr==0:
#         maxk=max(maxk,k)
#     else:
#         k=0
#         kr=0
#         ka=0
# print(maxk)

# for i in range(10):
#     for j in range(10):
#         s='12345'+str(i)+'7'+str(j)+'8'
#         s=int(s)
#         if s%68==0:
#             print(s,s//68)

