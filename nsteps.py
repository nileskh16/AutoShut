point = 0
t = input()
for i in range(0, t):
	coords = raw_input()
	x = int(coords.split()[0])
	y = int(coords.split()[1])
	
	if y == x or y == x-2:
		if x%2 != 0:
			point = x+y-1
		elif x%2 == 0:
			point = x+y
		
		print point
	else:
		print "No Number"