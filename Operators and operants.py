print(8%3) #remender modulus
print(8/3)
print(8//8) #floor division
print(2**5)  #square exponentiation
print(3>2)
print(3<2)
print(3==2)
print(3!=2) #not equal to
print(3>=2)
print(3<=2)

#LOGICAL OPERATORS
print(3>4 or 3<4)
print (not(3>4 or 3<4))
print (3>4 and 3<4)

#assingnment operators
# += add the current value
# -= sub the current value
# *= multiplye the current value


#identity operators  (is) (is not)
a= 1234
b= "1234"
print (a is b)
print (a is not b)

#bitwise operators
#compare the binary numbers
# AND (&) 0,0=0   0,1=0   1,0=0   1,1=1
a=10
b=8
print (a and b)

# OR ()  0,0=0   1,0=1  0,1=1   1,1=1
a=10
b=8
print (a or b)

#XOR (^)  0,0=0  0,1=1   1,0=1  1,1=1
a=10
b=8
print (a ^ b)

#ZERO fill left shift
a=10
b=8
print (a >> b)
#ZERO fill right shift
a=10
b=8
print (a << b)

print (bin(15))

#MEMBERS OPERATORS
#IN
a= "hello"
print ("e" in a)
#NOT IN
a= "hello"
print ("e" not in a)