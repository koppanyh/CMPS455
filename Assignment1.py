#CMPS 455 Assignment No. 1
#Authors: Mark Anderson, Koppany Horvath
#Language: Python 2.7
#Task: Write a program to read a postfix expression with $ at the end, compute and display its value (all variables are single letters of type integer)

while True: #repl loop
	variables = {} #hold vars so we only type them once
	stack = [] #hold the numbers for postfix operations

	inp = raw_input("Enter a postfix expression with a $ at the end:") #get user input

	for char in inp: #look through each character
		if char == "$": #print answer finish if $
			print "\tFinal value = %d" % stack.pop(-1)
			break
		elif char.isalpha(): #if it's a variable
			if not char in variables: #if variable not defined then define it
				var = raw_input("Enter the value of " + char + ":")
				variables[char] = int(var) #store int variable
			stack.append(variables[char]) #push to stack
		elif char in ["+","-","*","/"]: #if it's a math operation
			b = stack.pop(-1) #get b
			a = stack.pop(-1) #get a
			if char == "+": stack.append(a + b) #a + b
			elif char == "-": stack.append(a - b) #a - b
			elif char == "*": stack.append(a * b) #a * b
			elif char == "/": stack.append(a / b) #a / b
		else: #error, unknown character
			print "The character '" + char + "' is not valid, exiting"
			break
	
	inp = raw_input("Continue(Y/n)?") #ask to continue
	if inp.lower() == "n": break #break if not
	print

""" Output:
Enter a postfix expression with a $ at the end: ab*c+$
Enter the value of a: 2
Enter the value of b: 3
Enter the value of c: 4
	Final value = 10
Continue(Y/n)? y

Enter a postfix expression with a $ at the end: beef*++$
Enter the value of b: 2
Enter the value of e: 3
Enter the value of f: 4
	Final value = 17
Continue(Y/n)? n
"""
