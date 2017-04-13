try:
	t = input()
	for i in range(0, t):
		fl = map(int, raw_input().split())
		sl = map(int, raw_input().split())
		needed = fl[0]
		#print needed
		offers = fl[1]
		sl.sort(reverse=True)
		sum = 0
		counter = 0
		flag = True
		for j in range(0, offers):
			sum += sl[j]
			counter += 1
			#print sum 
			if sum >= needed:
				flag = False
				break
		print "Scenario #%d:" %(i+1)
		if flag:
			print "impossible"
		else:
			print counter
		print
except:
	pass
