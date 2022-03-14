#¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))
def f(x,A):
    return x%A==0

A=1
while True:
    for x in range(1,1000000):
        if not(not(f(x,A))or not(f(x,6))or f(x,42)):
            break
    else:
        print(A)
    A+=1
