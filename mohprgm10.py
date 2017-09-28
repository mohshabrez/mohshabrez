#! /usr/bin/python3
n=int(input("Enter an integer:"))
#the command enters the integer
print("The divisors of the number are:")
#guess it will display the divisors of the given integer by the for loop
for i in range(1,n+1):
    if(n%i==0):
        print(i)
