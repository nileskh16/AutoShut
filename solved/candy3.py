try:
	t = input()
	nl = raw_input()
	for i in range(0, t):
		sum = 0
		buff = 0
		counter = 0
		while(1):
			try:
				buff = input()
				sum = sum+buff
				counter += 1
			except: 
				break
		if sum%counter == 0:
			print "YES"
		else:	
			print "NO"
except:
	pass
	
