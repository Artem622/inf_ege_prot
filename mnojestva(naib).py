
P=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q=[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
def f(x,A):
    return ((x in  A) <=(x  in   P)) and ((x  in  Q) <= (not(x  in  A)))
A=set(range(1,10000))
for x in range(1,10000):
    if not f(x,A):
        A.remove(x)
print(len(sorted(A)))
