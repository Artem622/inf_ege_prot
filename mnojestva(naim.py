P=[2, 4, 6, 8, 10, 12]
Q=[3, 6, 9, 12, 15]
def f(x,A):
    return (x in P) <= (((x in Q) and not(x in A)) <= (not(x in P)))
A=set()
for x in range(1,10000):
    if not f(x,A):
        A.add(x)
print(sum(sorted(A)))

#(x ∈ {2, 4, 6, 8, 10, 12}) → (((x ∈ {3, 6, 9, 12, 15}) ∧ ¬(x ∈ A)) → ¬(x ∈ {2, 4, 6, 8, 10, 12}))