try:
	t=input()
	result = 'TAK'
	while t>1:
		if t%2 == 0:
			t = t/2
			if t==3:
				result = 'NIE'
				break
		else:
			t = 3*t+3
			if t==12: 
				result = 'NIE'
				break
	print result

except:
	pass
