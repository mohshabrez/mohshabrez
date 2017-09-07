#!/usr/bin/python3
#guess what the program does????
import random 
dice==0
while dice <101:
 	dice=random.randint(1,6)#gives random num
	print(dice)
	name="dice"
	print(name)
	while dice<3: dice=2
	print("get on ladder")
	if dice<7: dice=6
	print("near to ladder")
	if dice<2: dice=1
	print("get on the ladder")
	if dice<7: dice=6
	print("get on the ladder")
	if dice<3: dice=2
	print("get on the ladder")
	if dice<4: dice=3
	print("congratulations you win")