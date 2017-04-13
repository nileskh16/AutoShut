tcs = input()
for i in range(0, 2*tcs-1):
	ins = raw_input()
        if ins.isdigit():
		acts = int(ins)	 
		dict = {}
		for j in range(0, acts):
			acn = raw_input()
			if dict.get(acn) is None:
				dict[acn] = 1
			elif int(dict.get(acn)) > 0:
				'''cur = int(dict.get(acn))
				cur += 1
				print cur
				dict.set(acn, cur)'''
				dict[acn] += 1
		
		sortd = sorted(dict)
		print
		for key in sortd:
			print str(key) + " " + str(dict.get(key))
	else:
		pass
