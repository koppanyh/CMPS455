#CMPS 455 Assignment No. 2
#Authors: Mark Anderson, Koppany Horvath
#Language: Python 2.7
#Task: Write a program to find the value of a postfix expression. Variables are one or more characters.

def getTokens(inputStr): #function that splits input into individual parts
	tokens = inputStr.split(" ") #split by spaces
	tokens = [x for x in tokens if len(x) > 0] #filter out empty strings
	return tokens
def isNumber(num): #check if string represents an int
	try: #return true if yes
		int(num)
		return True
	except: #return false if no
		return False

while True: #repl loop
	variables = {} #hold vars so we only type them once
	stack = [] #hold the numbers for postfix operations

	inp = raw_input("Enter a postfix expression with a $ at the end:") #get user input
	tokens = getTokens(inp) #split the input up into small pieces for processing

	for char in tokens: #look through each token
		if char == "$": #print answer and finish if $
			print "\tFinal value = %d" % stack.pop(-1)
			break
		
		elif isNumber(char): #if it's a number
			stack.append(int(char)) #push it to the stack
		
		elif char in ["+","-","*","/"]: #if it's a math operation
			b = stack.pop(-1) #get b
			a = stack.pop(-1) #get a
			if char == "+": stack.append(a + b) #a + b
			elif char == "-": stack.append(a - b) #a - b
			elif char == "*": stack.append(a * b) #a * b
			elif char == "/": stack.append(a / b) #a / b
		
		else: #anything else is a variable
			if not char in variables: #if variable not defined then define it
				var = raw_input("Enter the value of " + char + ":")
				variables[char] = int(var) #store int variable
			stack.append(variables[char]) #push to stack
	
	inp = raw_input("Continue(Y/n)?") #ask to continue
	if inp.lower() == "n": break #break if not
	print

""" Output:
Enter a postfix expression with a $ at the end: 20 num1 45 + tom - * $
Enter the value of num1: 10
Enter the value of tom: 5
	Final value = 1000
Continue(Y/n)? y

Enter a postfix expression with a $ at the end: myscore yourscore 45 + 100 + * $
Enter the value of myscore: 3
Enter the value of yourscore: 5
	Final value = 450
Continue(Y/n)? n
"""
