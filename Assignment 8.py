#CMPS 455 Assignment No. 8
#Authors: Koppany Horvath
#Language: Python 3.6
#Task: Given the following CFG and the LR Parsing table. Write a program to trace input strings (1) (i+i)*i$ (2) (i*)$. A sample I/O is shown on the back

def matches(string):
	parseTable = [
		{'i':'s5','+':None,'-':None,'*':None,'/':None,'(':'s4',')':None, '$':None,'E':'1', 'T':'2', 'F':'3' }, #0
		{'i':None,'+':'s6','-':'s7','*':None,'/':None,'(':None,')':None, '$':True,'E':None,'T':None,'F':None}, #1
		{'i':None,'+':'r3','-':'r3','*':'s8','/':'s9','(':None,')':'r3', '$':'r3','E':None,'T':None,'F':None}, #2
		{'i':None,'+':'r6','-':'r6','*':'r6','/':'r6','(':None,')':'r6', '$':'r6','E':None,'T':None,'F':None}, #3
		{'i':'s5','+':None,'-':None,'*':None,'/':None,'(':'s4',')':None, '$':None,'E':'10','T':'2' ,'F':'3' }, #4
		{'i':None,'+':'r8','-':'r8','*':'r8','/':'r8','(':None,')':'r8', '$':'r8','E':None,'T':None,'F':None}, #5
		{'i':'s5','+':None,'-':None,'*':None,'/':None,'(':'s4',')':None, '$':None,'E':None,'T':'11','F':'3' }, #6
		{'i':'s5','+':None,'-':None,'*':None,'/':None,'(':'s4',')':None, '$':None,'E':None,'T':'12','F':'3' }, #7
		{'i':'s5','+':None,'-':None,'*':None,'/':None,'(':'s4',')':None, '$':None,'E':None,'T':None,'F':'13'}, #8
		{'i':'s5','+':None,'-':None,'*':None,'/':None,'(':'s4',')':None, '$':None,'E':None,'T':None,'F':'14'}, #9
		{'i':None,'+':'s6','-':'s7','*':None,'/':None,'(':None,')':'s15','$':None,'E':None,'T':None,'F':None}, #10
		{'i':None,'+':'r1','-':'r1','*':'s8','/':'s9','(':None,')':'r1', '$':'r1','E':None,'T':None,'F':None}, #11
		{'i':None,'+':'r2','-':'r2','*':'s8','/':'s9','(':None,')':'r2', '$':'r2','E':None,'T':None,'F':None}, #12
		{'i':None,'+':'r4','-':'r4','*':'r4','/':'r4','(':None,')':'r4', '$':'r4','E':None,'T':None,'F':None}, #13
		{'i':None,'+':'r5','-':'r5','*':'r5','/':'r5','(':None,')':'r5', '$':'r5','E':None,'T':None,'F':None}, #14
		{'i':None,'+':'r7','-':'r7','*':'r7','/':'r7','(':None,')':'r7', '$':'r7','E':None,'T':None,'F':None}, #15
	]
	cfg = [
		None,
		{"nTerm": "E", "popLen": 6}, #(1) E=E+T
		{"nTerm": "E", "popLen": 6}, #(2) E=E-T
		{"nTerm": "E", "popLen": 2}, #(3) E=T
		{"nTerm": "T", "popLen": 6}, #(4) T=T*F
		{"nTerm": "T", "popLen": 6}, #(5) T=T/F
		{"nTerm": "T", "popLen": 2}, #(6) T=F
		{"nTerm": "F", "popLen": 6}, #(7) F=(E)
		{"nTerm": "F", "popLen": 2}, #(8) F=i
	]
	stack = []
	curTerm = None
	curNonTerm = None
	curIndex = 0
	canRead = True

	stack.append(0)

	while True:
		curIndex = stack.pop()
		if(canRead):
			curTerm = string[0]
			string = string[1:]
			curNonTerm = curTerm
			print("Read:", curTerm, " - ", "Stack:", stack)
		item = parseTable[curIndex][curNonTerm]
		if item == None: return False
		elif item == True: return True
		elif item[0] == 's':
			canRead = True
			stack.append(curIndex)
			stack.append(curNonTerm)
			stack.append(int(item[1:]))
		elif item[0] == 'r':
			canRead = False
			stack.append(curIndex)
			item = cfg[int(item[1:])]
			curNonTerm = item["nTerm"]
			for _ in range(item["popLen"]): stack.pop()
		else:
			stack.append(curIndex)
			stack.append(curNonTerm)
			stack.append(int(item))
			curNonTerm = curTerm
	return False

for s in ["(i+i)*i$", "(i*)$"]:
	print("Working on string:", s)
	if matches(s): print("String matches grammar!")
	else: print("Error: string does not match grammar!")
	print()

""" Output:
Working on string: (i+i)*i$
Read: (  -  Stack: []
Read: i  -  Stack: [0, '(']
Read: +  -  Stack: [0, '(', 4, 'i']
Read: i  -  Stack: [0, '(', 4, 'E', 10, '+']
Read: )  -  Stack: [0, '(', 4, 'E', 10, '+', 6, 'i']
Read: *  -  Stack: [0, '(', 4, 'E', 10, ')']
Read: i  -  Stack: [0, 'T', 2, '*']
Read: $  -  Stack: [0, 'T', 2, '*', 8, 'i']
String matches grammar!

Working on string: (i*)$
Read: (  -  Stack: []
Read: i  -  Stack: [0, '(']
Read: *  -  Stack: [0, '(', 4, 'i']
Read: )  -  Stack: [0, '(', 4, 'T', 2, '*']
Error: string does not match grammar!
"""
