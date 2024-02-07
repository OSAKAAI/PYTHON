#write a program to append the numbers in the list and print every no that even or odd
dict1={"name":"Vaibhav","age":"20","canvote":"true"}
tuple1=(("parrot","sparrow","Lion","tiger"))
print(tuple1)
print(dict1)
num=[]
print("Enter the 10 numbers")
for i in range(11):
    n=int(input(""))
    num.append(n)
print(num)
          
for j in num:
  if j % 2 == 0:
     print(f"{j} is even number")
  else:
     print(f"{j} is odd number")

      
