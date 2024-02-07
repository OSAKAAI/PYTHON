n=7
print("welcome to guess the number game\ntake the guess to our secret number and you will won nothing(not the phone nothing)\n your  hints are ")
print("hint: bole jo koyal bagho me")
i=int(input("take your frist guess for the secret number\n"))
if i == n:
    print("your guess is right")
else:
    print("your frist guess was wrong")
    j=int(input("take your second  guess for the secret number\n"))
    if j==n:
        print("your guess is right")
    else:
        print("your second guess was wrong")
        k=int(input("take your third guess for the secret number\n"))
        if k==n:
            print("your guess is right")
        else:
            print("your third guess was wrong")
            print("you lost")
            
