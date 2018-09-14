#CMPS 455 Assignment No. 3 Pt. 2
#Authors: Mark Anderson, Koppany Horvath
#Language: Python 3.6
#Task: Write a program to determine whether an input string is accepted.
#      S -> aS | bB | cC
#      B -> bB | aC | cD | lambda
#      C -> aS | (b+c)D | lambda
#      D -> bD | aB | cC

def S(s): #s node, start, S ->
	if s == "": return False #don't accept lambda
	if s[0] == "a": return S(s[1:]) # aS
	if s[0] == "b": return B(s[1:]) # bB
	if s[0] == "c": return C(s[1:]) # cC
	return False #unknown input
def B(s): #b node, end, B ->
	if s == "": return True #accept lambda
	if s[0] == "b": return B(s[1:]) # bB
	if s[0] == "a": return C(s[1:]) # aC
	if s[0] == "c": return D(s[1:]) # cD
	return False #unknown input
def C(s): #c node, end, C ->
	if s == "": return True #accept lambda
	if s[0] == "a": return S(s[1:]) # aS
	if s[0] == "b" or s[0] == "c": return D(s[1:]) # (b+c)D
	return False #unknown input
def D(s): #d node, D ->
	if s == "": return False #don't accept lambda
	if s[0] == "b": return D(s[1:]) # bD
	if s[0] == "a": return B(s[1:]) # aB
	if s[0] == "c": return C(s[1:]) # cC
	return False #unknown input

def accreg(s): #tell us if input is accepted or not
	o = S(s)
	if o: o = "Accepted"
	else: o = "Rejected"
	print(s, ":", o)

w1 = "abbbcaaa"
w2 = "ccccbbb"
w3 = "aabbcbbb"

accreg(w1)
accreg(w2)
accreg(w3)

""" Output:
abbbcaaa : Rejected
ccccbbb : Rejected
aabbcbbb : Rejected
"""
