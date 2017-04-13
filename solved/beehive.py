import math
try:
	while True:
		num = input()
		if num == -1:
			break
		valid = (4*num - 1)/3
		if math.sqrt(valid) - int(math.sqrt(valid)) == 0:
			print 'Y'
		else:
			print 'N'	
			
except:
	pass
