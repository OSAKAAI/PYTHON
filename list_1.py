list_1=[10,20,45,78,'vaibhav','bhai','op','hai']
list4=['one','two' , "three"] # List of strings
list5=['SHYAM', 25 ,[50, 100],[150, 90]] # Nested Lists
list6=[100,'Ram',17.765] # List of mixed data types
list7 = ['DHARMANDRA', 25 ,[50, 100],[158, 90],{'Johnny Bravo' ,'BHUPENDRA'}]
print(len(list_1)) #Length of List 
print(list6)
print(list5[0]) # Retreive first element of the List
print(list4[2]) # Retreive first element of the List
print(list4[-2])
print(list4[-1]) # Last item of the List
print(list5[-1]) # Last item of the List

print(" ")

mylist = ['SIYA' , 'PATI' , 'RAM' , 'CHANDRA' , 'KI' , 'JAI' , 'OHM' , 'Shanti']
print(mylist[0:3]) 
print(mylist[2:5])
print(mylist[:3])
print(mylist[:2])
print(mylist[-3:])
print(mylist[-2:])

print(" ")

mylist.append('OHM') # Add an item to the end of the List
print(mylist)
mylist.insert(9,':D') # Add item at index Location 9
print(mylist)
mylist.insert(1,'ONE') # Add item at index Location 1
print(mylist)

print(" ")

mylist.remove('ONE') # Remove item "ONE"
print(mylist)
mylist.pop() # Remove Last item of the List
print(mylist)
del mylist[7] # Remove item at index Location 7
print(mylist)





#SWAP THE FIRST AND THE LAST ELEMENT
mass=['monkey','king','is','the','god']
a=mass[0]
mass[0]=mass[4]
mass[4]=a
print(mass)

#
digits = []
for i in range(10):
    digit = int(input("Enter the number: "))
    digits.append(digit)
maximum = digits[0]
for j in range(1, 10):
    if digits[j] > maximum:
        maximum = digits[j]
print("The maximum digit is:", maximum)

 
