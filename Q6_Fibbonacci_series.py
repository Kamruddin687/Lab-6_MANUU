a = -1
b = 1
print("For Fibbonacci series")
terms = input("Enter no of terms U want-: ")
while 1:
    try:
        terms = int(terms)
        print("The Fibbonacci series formed is-:")
        for i in range(terms):
            c = a+b
            print(c)
            a = b 
            b = c 
        break
    except ValueError:
        print("Enter number only")
        break
