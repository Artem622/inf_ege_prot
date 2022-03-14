P=[2, 4, 6, 8, 10, 12]
Q=[]
def f(x,A):
    return (x in A) <= (x**2 <= 81) and (y**2 in Q) <= (y in A):
A=set()
for x in range(1,10000):
    if not f(x,A):
        A.add(x)
print(sum(sorted(A)))
