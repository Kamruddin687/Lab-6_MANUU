print("To find individual Sum of given numbers") # Eg-: 123 => 1+2+3 => 6
sum=0
while 1:
    n = input("Enter the number you Want:- ")
    try:
        n = int(n)
        while(n>0):
            a = n % 10
            sum = sum + a
            n = n//10
        print("Individual sum of given number is-:",sum)
        break
    except ValueError:
        print("Enter number only")
        continue

    
