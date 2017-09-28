#!/usr/bin/python3
choice=["1","2","3"]
	choice = input ("enter p to choice")
	#here we enter our choice
		cpu choice = choice[random.randint(1,3)]
		# the command accepts the choice n plays with cpu
		if choice==stone:
			choice=paper
			print("stone caugght paper",choice)
			#this command decide whether who wins
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
		
		       	
