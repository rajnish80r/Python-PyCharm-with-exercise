#For Loops
for v in range(1,9,2):
    print(v)

#Table example
n= int(input("enter the number: "))
for v in range(1,11):
    print (n,"*",v,"=",n*v)

#While Loop
n=0
while n<=5:
    print(n)
    n+=1

n=1
a=9
while n<=10:
    print(a, "x",n,"=", n*a)
    n+=1

#while-true loop
while True:
    num1=int(input('enter a number: '))
    num2=int(input('enter another number: '))
    print(num1+num2)
    repeat= input('Do you want to break the program?: ')
    if repeat== "yes" or "Yes" or "YES" :
        break

#Nested Loops loop inside the loops
for i in range (1,4):
    for j in range(1,11):
        print(j, end ="")
    print()

# for pattern 1 to 9
for i in range (1,10):
    for j in range(1,i+1):
        print(j, end =" ")
    print()

#break and continue statement
for i in range (1,11):
    if i == 5:
        continue
    else: print(i)
    if i == 7:
        break