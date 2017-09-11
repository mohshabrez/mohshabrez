#!/usr/bin/python3
choice=["1","2","3"]
	choice = input ("enter p to choice")
		cpu choice = choice[random.randint(1,3)]
		if choice==stone:
			choice=paper
			print("stone caugght paper",choice)
		else:
			print("cpu wins")
		if choice==paper:
			choice=scissor
			print("scissor cuts the paper",choice)
		else:
			print("cpu wins")
		if choice==scissor:
		    choice=stone
		    print("stone hits the scissor",choice)
		else:
			print("cpu wins")
		
		       	