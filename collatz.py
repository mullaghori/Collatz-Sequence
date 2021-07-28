
try:
	integer = int(input())
	def callatz(number):
		while number != 1:
			if number % 2 == 0:
				number = number // 2
				print(number)
			else:
				number = 3 * number + 1
				print(number)
	callatz(integer)
except ValueError:
		print('You have entered a non-integer value! \nIn order to run the code, you must enter an integer value!')
		print('Thank you 😊!')
		