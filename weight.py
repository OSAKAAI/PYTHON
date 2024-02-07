weight=float(input("Enter your weight\n"))
unit=input("Kg or lbs\n")
wi=weight
if unit == "kg":
    weight =weight /0.45
    print("weight in lbs", weight,"lbs")
    wg=wi*1000
    print("weight in grams : ",wg)
else:
        weight=weight*0.45
        print("weight in kg", weight,"Kg")
        
    
