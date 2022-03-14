A=0
while True:
     for x in range(1000000):
          if not(((x & 49 ==0)<=((x & 28 != 0)<=(x & A !=0)))):
               break
     else:
          print(A)
     A+=1
          
#x & 49 = 0 → (x & 28 ≠ 0 → x & А ≠ 0)
 



 
