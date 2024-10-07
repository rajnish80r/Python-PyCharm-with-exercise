#if statement
marks=100
if marks>90:
    print ('You have selected')

#if-else Statement
dis=50
if dis>60:
    print('Qualified')
else:
    print('Disqualified')

#If-Elif-Else Statement multiple statement
mark= 68
if mark>70:
    print("You will go for a trip")
elif mark>=65 and mark<=70:
    print('you will get a ticket')
else:
    print("Sorry, Nothing for you")

    #nested-if Statement (If statement can be repeated for multiple times)
    marks=87
if marks >=80:
    print('you can play games')
    if marks>=64 and  marks<=70:
        print('you can watch TV')
        if marks>=50 and marks<=64:
            print('you can sleep')
else:
    print('NO rest')

#Short-Hand-If statement
marks=87
if marks>=90: print("you can go with friend")
else: print("no fun with friends")

#shaot-if-else statement
marks=97
print("you can play videos games") if marks>=90 else print("no video games")
