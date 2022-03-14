a=list(map(int,open("C:/Users/Artem/Downloads/17.11.t.txt").readlines()))
m=-500000000
count=0
for i in range(len(a)-1):
    if (a[i]%5==0 or a[i+1]%5==0) and (a[i]+a[i+1])%7==0:
        count+=1
        m=max(m,a[i]+a[i+1])
print(count,m)
