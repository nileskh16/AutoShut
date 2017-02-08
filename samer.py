a = 0
def doit():
	global a
	a = input()
	if a<= 0:
		return False
	else:
		return True
while(doit()):
	nos = 0
	for j in range(1, a+1):
		nos = nos + j*j
	print nos
	
#9920425902