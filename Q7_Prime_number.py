n = input("Enter the number of terms to print prime number=")
while 1:
    try:
        n = int(n)
        if n==1:
            print("1 is not a Prime no")
            break
        print("The prime number are here:")
        for val in range(2,n+1):     
           if val > 1: 
               for n in range(2, val): 
                   if (val % n) == 0: 
                       break
               else: 
                   print(val,end=" ")
        break
    except ValueError:
        print("Enter number only")
        break
