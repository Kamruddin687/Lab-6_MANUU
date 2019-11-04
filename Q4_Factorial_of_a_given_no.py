print("To find factorial of a given number")
factorial = 1
while 1:
    num = input("Enter a number you want-: ")
    try:
        num = int(num)   
        if num < 0:
           print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
           print("The factorial of 0 is 1")
        else:
           for i in range(1,num + 1):
               factorial = factorial*i
           print("The factorial of",num,"is",factorial)
           break
    except ValueError:
        print("Enter number only")
        continue
