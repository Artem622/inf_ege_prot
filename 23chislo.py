A=set()
def f(x,count):
    if count==3:
        A.add(x)
        return
    elif count>3:
        return
    else:
        return f(x+2,count+1) or f(x*3,count+1)
f(2,0)
print(A)

