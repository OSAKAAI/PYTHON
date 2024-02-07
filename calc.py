def arith(num1,num2,op):
    if op == '+' :
     sum=num1+num2
     print("addition is " , sum )
    elif op == '-' :
     sub=num1-num2
     print("substraction is " , sub )
    elif op == '*' : 
     mul=num1*num2
     print("multiplication is " , mul )
    elif op == '/' :
     div=num1/num2
     print("division is " , div )
    else :
     print("wrong choice input")
    
a=int(input("Enter no first "))
b=int(input("Enter no sec "))
print('''   ****MENU****
       For Adddition of two no's |  +
       For substraction of two no's |  -
       For Multiplication of two no's |  *
       For division of two no's |  /
                                      ''')

op=input("enter the operation you want to do with the two no's ")            
arith(a,b,op)
