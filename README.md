# Collatz-Sequence
It's a practice project for python beginners! 

No.1 Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number//2 and return this value. 
If the number is odd, the collatz() should print and return 3*number+1.

No.2 Then write a program that let's user type in an integer and that keeps calling collatz() on the number until the function returns the value 1.

#amazingly enough, this sequence actually works for any integer. Sooner or later, using this sequence you'll arrive at 1. Even mathematicians aren't sure why?. Your program is exploring what's called the collatz sequence. Sometimes called the "simplest impossible math problem".

NOTE: Remember to convert the return value from input() to an integer with the int() function. Otherwise it will be a string value.

HINT: An integer number is even if number%2==0 and it's odd, if number%2==1.

👉 The output of this program could look something like this:

 
