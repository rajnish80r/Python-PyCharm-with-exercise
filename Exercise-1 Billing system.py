while True:
    name=input("enter costumer name: ")
    total=0
    while True:
        print("enter the amount and quantity: ")
        amount= float(input("enter amount: "))
        quantity= float(input("enter the quantity: "))
        total += amount*quantity
        repeat= input('Do you want to buy mor items?: ')
        if repeat== "no" or repeat == "No":
            break
    print("-",20)
    print("name: ", name)
    print("total amount to be paid: ", total)
    print("-",20)
    print("***********Thank You for Shopping***********")
    repeat1= input("Do you want to go to next costumer?: (Yes/No): ")
    if repeat1== "no" or repeat1== "No":
        break


