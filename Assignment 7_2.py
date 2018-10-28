#CMPS 455 Assignment No. 7 Pt. 2
#Authors: Koppany Horvath
#Language: Python 3.6
#Task: Write a program to determine which of the following are accepted or rejected by the grammar: (i) a=(a+a)*b$ (ii) a=a*(b-a)$ (iii) a=(a+a)b$

def matches(string):
	string = string.replace("a=","q") #use q to represent a=
	parseTable = {
		"S":{"q":"qE", "a":None, "b":None, "+":None,  "-":None,  "*":None,  "/":None,  "(":None,  ")":None, "$":None},
		"E":{"q":None, "a":"TQ", "b":"TQ", "+":None,  "-":None,  "*":None,  "/":None,  "(":"TQ",  ")":None, "$":None},
		"Q":{"q":None, "a":None, "b":None, "+":"+TQ", "-":"-TQ", "*":None,  "/":None,  "(":None,  ")":"",   "$":""},
		"T":{"q":None, "a":"FR", "b":"FR", "+":None,  "-":None,  "*":None,  "/":None,  "(":"FR",  ")":None, "$":None},
		"R":{"q":None, "a":None, "b":None, "+":"",    "-":"",    "*":"*FR", "/":"/FR", "(":None,  ")":"",   "$":""},
		"F":{"q":None, "a":"a",  "b":"b",  "+":None,  "-":None,  "*":None,  "/":None,  "(":"(E)", ")":None, "$":None}
	}
	stack = []
	curTerm = None
	curNonTerm = None
	done = False
	isGood = True

	stack.append("$")
	stack.append("S")

	while not done:
		curTerm = string[0] #read
		string = string[1:]

		while 1:
			curNonTerm = stack.pop()
			if curNonTerm in "qab+-*/()$": #if it's a term, match
				print("Match:", curNonTerm.replace("q","a="), " - ", "Stack:", stack)
				if curNonTerm == "$": done = True #if it's the end then exit
				break

			p = parseTable[curNonTerm][curTerm]
			if p == "": continue #if it's lambda, pop again
			elif p == None: #if it's none, break with error
				done = True
				isGood = False
				break

			for x in p[::-1]: stack.append(x) #push in reverse order
	return isGood

for s in ["a=(a+a)*b$","a=a*(b-a)$","a=(a+a)b$"]:
	print("Working on string:", s)
	isMatch = matches(s)
	if isMatch: print("String matches grammar!")
	else: print("Error: string does not match grammar!")
	print()

""" Output:
Working on string: a=(a+a)*b$
Match: a=  -  Stack: ['$', 'E']
Match: (  -  Stack: ['$', 'Q', 'R', ')', 'E']
Match: a  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'R']
Match: +  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'T']
Match: a  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'R']
Match: )  -  Stack: ['$', 'Q', 'R']
Match: *  -  Stack: ['$', 'Q', 'R', 'F']
Match: b  -  Stack: ['$', 'Q', 'R']
Match: $  -  Stack: []
String matches grammar!

Working on string: a=a*(b-a)$
Match: a=  -  Stack: ['$', 'E']
Match: a  -  Stack: ['$', 'Q', 'R']
Match: *  -  Stack: ['$', 'Q', 'R', 'F']
Match: (  -  Stack: ['$', 'Q', 'R', ')', 'E']
Match: b  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'R']
Match: -  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'T']
Match: a  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'R']
Match: )  -  Stack: ['$', 'Q', 'R']
Match: $  -  Stack: []
String matches grammar!

Working on string: a=(a+a)b$
Match: a=  -  Stack: ['$', 'E']
Match: (  -  Stack: ['$', 'Q', 'R', ')', 'E']
Match: a  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'R']
Match: +  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'T']
Match: a  -  Stack: ['$', 'Q', 'R', ')', 'Q', 'R']
Match: )  -  Stack: ['$', 'Q', 'R']
Error: string does not match grammar!
"""
