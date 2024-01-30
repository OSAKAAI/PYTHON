n=int(input("Enter the number "))
digits = len(str(n))
original = n
s = 0
while n != 0:
    r=n%10
    s=s+r**digits
    n=n//10
if original == s:
        print(f"{original} is a armstrong no")
else:
        print(f"{original} is not a armstrong no")
              
