try:
	t = input()
	for i in range(0, t):
		nl = raw_input()
		eq = raw_input()
		opr = eq.split()
		a = opr[0]
		b = opr[2]
		c = opr[4]
		if 'machula' in c:
			print a + " + " + b + " = " + str(int(a) + int(b))
		elif 'machula' in a:
			print str(int(c) - int(b)) + " + " + b + " = " + c
		elif 'machula' in b: 
			print a + " + " + str(int(c) - int(a)) + " = " + c
except:
	pass
