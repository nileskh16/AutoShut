try:
	space = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
	t = input()
	for i in range(t):
		rs = ''
		result = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT':0, 'HHH':0}
		num = input()
		seq = raw_input()
		for j in range(len(seq)-2):
			result[seq[j:j+3]] += 1
		for sample in space:
			rs += '%d ' %(result.get(sample))
		print '%d %s' %(num, rs)
except:
	pass