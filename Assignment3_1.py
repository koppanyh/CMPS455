#CMPS 455 Assignment No. 3 Pt. 1
#Authors: Mark Anderson, Koppany Horvath
#Language: Python 3.6
#Task: Write a program to read one token at a time from the given text file and determine whether the token is:
#    a number
#    an identifier (must start with an underscore or a letter, followed by more letters, more digits, or more underscores)
#    a reserved word. string reserved[5] = {"while","for","switch","do","return"};

f = open("tokens.txt","r") #open the token text file

def gettoken(): #get the next token each time
	t = f.readline()
	if t == "": return None #return none if no tokens left
	return t.strip() #remove trailing spaces and newlines

def isReserved(token): #tell us if it's a reserved word
	return token in ["while","for","switch","do","return"]
def isInt(token): #use this rule to see if it's a number [-]d{d}
	if token[0] == "-": token = token[1:] #remove optional - from beginning
	if token == "": return False #if that's the only character, then no
	for c in token: #check that each char is digit, else no
		if not c.isdigit(): return False
	return True #yes if it passed all tests
def isIdentifier(token): #tell us if it's an identifier (a|_){a|d|_}
	if not token[0] == "_" and not token[0].isalpha(): return False #check that the first char is alpha or _
	for c in token: #check that each character is alpha or digit or _
		if not c.isalpha() and not c.isdigit() and c != "_": return False
	return True #yes if passed all tests

def yesNo(b): #format true false to yes/no
	if b: return "Yes"
	else: return "No"

results = [] #list of results of each token
maxToken = 5 #for formatting table
while True:
	token = gettoken() #get the token
	if token == None: break #finish if none left
	if len(token) > maxToken: maxToken = len(token) #hold size of largest token for table formatting
	flags = [ #save data
		token,
		yesNo(isInt(token)), #if it's a number
		yesNo(isIdentifier(token)), #if it's an identifier
		yesNo(isReserved(token)) #if it's reserved
	]
	results.append(flags)
maxToken += 3 #make it just a little bigger
formatStr = "{:<"+str(maxToken)+"}{:<8}{:<12}{:<12}" #create formatting string for nice output

print(formatStr.format("Token", "Number", "Identifier", "Reserved")) #print header
for rez in results: #print each output from the result list
	print(formatStr.format(rez[0], rez[1], rez[2], rez[3]))

f.close() #close the text file now that we're done

""" Output:
Token      Number  Identifier  Reserved    
K-mart     No      No          No          
23andMe    No      No          No          
456        Yes     No          No          
Tax 2018   No      No          No          
While      No      Yes         No          
switch     No      Yes         Yes         
do_it      No      Yes         No          
_Fall_18   No      Yes         No          
_Jan 19    No      No          No
"""
