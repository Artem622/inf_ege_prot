a=list(map(int,open('C:/Users/Artem/Downloads/o1.txt').readlines()))
m=0
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])%2==1 and (a[i]*a[j])%3==0:
            count+=1
            m=max(m,a[i]+a[j])
print(count,m)