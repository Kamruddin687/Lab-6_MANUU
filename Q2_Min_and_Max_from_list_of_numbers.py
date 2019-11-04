print("To find the Maximum and Minimum element in a list")
while 1:
    list = []
    num = input("How many numbers you want in a list : ")
    try:
        num = int(num)
        for n in range(num):
            numbers = int(input("Enter number-:"))
            list.append(numbers)
        print("Maximum element in the list is :", max(list))
        print("Minimum element in the list is :", min(list))
        break
    except ValueError:
        print("Enter number only")
        continue

    
