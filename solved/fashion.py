try:
	t = input()
	for i in range(t):
		nums = input()
		men = map(int, raw_input().split())
		women = map(int, raw_input().split())
		men.sort(reverse=True)
		women.sort(reverse=True)
		sum = 0
		for j in range(nums):
			sum += men[j]*women[j]
		print sum

except:
	pass
