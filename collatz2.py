
try:
	integer = int(input("input num: "))
	def callatz(number):
		if number%2 == 0:
			return number//2
		else:
			return 3*number+1
	while(integer!=1):
 	   integer = callatz(integer)
 	   print(integer)
except ValueError:
		print('You have entered a non-integer value! \nIn order to run the code, you must enter an integer value!')
		print('Thank you 😊!')