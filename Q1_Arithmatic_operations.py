print("Performing Arithmatic operation's")
while 1:
    a = input("Enter the value of a-:")
    b = input("Enter the value of b-:")      
    try:
        a = int(a)
        b = int(b)
        Add = a + b          # Addition of numbers
        if a>b:
            Sub = a - b          # Subtraction of numbers
        else:
            Sub = b - a
        Mul = a * b          # Multiplication of number 
        Div1 = a / b         # Division(float) of number  
        Div2 = a // b        # Division(Type casting) of number  
        Mod = a % b          # Modulo of both number
        print("Sum of ",a," and ",b," is -:",Add) 
        print("Subtraction of ",a," and ",b," is -:",Sub) 
        print("Product of ",a," and ",b," is -:",Mul) 
        print("Division of ",a," and ",b," is -:",Div1) 
        print("Type casted division of ",a," and ",b," is -:",Div2) 
        print("Modulus of ",a," and ",b," is -:",Mod)
        break
    except ValueError:
        print(" Enter number only ")
        continue
