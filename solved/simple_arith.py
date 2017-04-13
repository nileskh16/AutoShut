try:
	t = input()
	for i in range(0, t):
		ln = raw_input()
		ops = raw_input().split()
		opns = ops[:len(ops)-1:2]
		result = long(opns[0])
		j = 1
		for op in ops[1:len(ops)-1:2]:
			if op == '+':
				result = result + long(opns[j])
				j += 1
			elif op == '-':
				result -= long(opns[j])
				j += 1
			elif op == '*':
				result *= long(opns[j])
				j += 1
			elif op == '/':
				result /= long(opns[j])
				j += 1
		print result
			
except Exception, err:
	print str(err)
	pass
