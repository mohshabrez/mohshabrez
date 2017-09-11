#!/usr/bin/python3
import random 


c=["1","2","3"]

print ("Please select:") 
print ("1  Rock") 
print ("2  Paper") 
print ("3  Scissors") 

player = input ("Choose from 1-3: ") 
CPU= c[random.randint(0,2)]

print("CPU choose",CPU)

if (player==CPU):
        print("draw")


if player == '1': 
    print ("You choose Rock")
    if(CPU==2):
        print("CPU wins")
    else:
        print("player wins")

if player == 3: 
    print ("You choose scissors") 
    sleep (2) 
    if(CPU==2):
        print("You win!")

    else: 
        print ("You choose Scissors") 
        sleep (2) 
        print ("CPU chooses Rock")  
        print ("You lose, and you will never win!")