p1,p2,q1,q2=2,20,15,25
P=[i/10 for i in range(p1*10,p2*10+1)]
Q=[i/10 for i in range(q1*10,q2*10+1)]

def f(x,A):
    return (((not(x in A))<=(not(x in P))) or (x in Q))
A=set()
for x in [i/10 for i in range(1,1000)]:
    if not f(x,A):
        A.add(x)
print(sorted(A))
