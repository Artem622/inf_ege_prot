def vodka(x,a,b):
    s=''
    x=int(str(x),a)
    while x>0:
        s=s+ str(x%b)
        x=x//b
    return s[::-1]





print(vodka(211,10,5))
print(vodka(12,10,5))
print(vodka(13,10,5))
