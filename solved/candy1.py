try:
	while True:
		t = input()
		if t == -1:
			break
		items = [input() for x in range(t)]
		#items.sort(reverse=True)
		total = 0
		for item in items:
			total += item
		if total%t == 0:
			med = total/t
			nums = list(filter(lambda x: x<=med, items))
			diff = 0
			for num in nums:
				diff += (med-num)
			print diff
		else:
			print -1
except:
	pass
