a=list(map(int,open('C:/Users/Artem/Downloads/r5.txt').readlines()))
maxs=0
count=0
for i in range (len(a)-2):
    b=max(a[i],a[i+1],a[i+2])
    c=min(a[i],a[i+1],a[i+2])
    d=a[i]+a[i+1]+a[i+2]-b-c
    if b**2==c**2+d**2:
        count+=1
        maxs=max(maxs,b+c+d)
print(count,maxs)