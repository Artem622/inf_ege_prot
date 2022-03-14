import itertools

a=list(itertools.permutations('ГЕОРГИЙ',r=7))
k=0
for i in a:
    s=''.join(i)
    if s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3] and s[3]!=s[4] and  s[4]!=s[5] and s[5]!=s[6]:
        k+=1
print(k//2)

