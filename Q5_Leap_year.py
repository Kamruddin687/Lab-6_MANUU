print("To find Year is a leap year or not")
year = input("Enter a year: ")
while 1:
    try:
        year = int(year)
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print(year,"is a leap year")
                else:
                    print(year,"is not a leap year")
            else:
                print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
        break
    except ValueError:
        print("Enter number only")
        break
