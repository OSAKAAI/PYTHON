n=int(input("Enter the starting point of range "))
m=int(input("Enter the ending point of range   "))
for i in range(n,m):     
 digits = len(str(i))
 original = i
 s=0
 while i != 0:
    r=i%10
    s=s+r**digits
    i=i//10
 if original == s:
        print(f"{original} is a armstrong no")
 
              
