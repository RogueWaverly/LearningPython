import numpy as np

print("1.\tHello, World!")
print("2.\tRoll Die")
print("3.\tGuess a Number")
print("4.\tMad Libs")
choice = input("Pick a program: ")

if( choice==1 ):
	print("Hello, World!")

elif( choice==2 ):
	again = 1
	while( again ):
		roll = np.random.randint(1,7)
		print(roll)
		again = input("Would you like to roll again? (1/0) ")

elif( choice==3 ):
	def isNum(guess):
		try:
			return float(guess)
		except ValueError:
			return 0
	def diffBetween(num, guess):
		return num-guess
	def compare (num, guess):
		diff = diffBetween(num, guess)
		if( diff<0 ):
			print("Your number is too high.")
			return 0
		elif( diff>0 ):
			print("Your number is too low.")
			return 0
		else:
			print("That's correct!")
			return 1
	again = 1
	while( again ):
		num = np.random.randint(1,11)
		isCorrect = 0
		while( not isCorrect ):
			guess = 0
			while( not guess ):
				guess = isNum(raw_input("Guess a number between 1 and 10: "))
			isCorrect = compare(num, guess)
		again = input("Would you like to play again? (1/0) ")

elif( choice==4 ):
	def isNum(guess):
		try:
			float(guess)
			return 1
		except ValueError:
			return 0
	again = 1
	while( again ):
		noun1 = raw_input("Enter a noun: ")
		noun2 = raw_input("Enter another noun: ")
		emotion1 = raw_input("Enter an emotion: ")
		emotion2 = raw_input("Enter another emotion: ")
		numString = raw_input("Enter a number: ")
		while( not isNum(numString) ):
			numString = raw_input("Enter a number: ")
		num = float(numString)

		print("Some say the world will end in %s," % noun1)
		print("Some say in %s." % noun2)
		print("From what I've tasted of %s" % emotion1)
		print("I hold with those who favor %s." % noun1)
		print("But if it had to perish %0.2f times," % num)
		print("I think I know enough of %s" % emotion2)
		print("To say that for destruction %s" % noun2)
		print("Is also great")
		print("And would suffice.")
		again = input("Would you like to play again? (1/0) ")