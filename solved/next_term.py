try:
	while True:
		nums = map(int, raw_input().split())
		if [0, 0, 0] == nums:
			break
		result, nt = '', 0
		'''cd, cr = 0, 1
		cd1 = nums[2] - nums[1]
		cd = cd1 if nums[2] - nums[1] == nums[1] - nums[0] else 0
		if 0 not in nums:
			cr1 = nums[2] // nums[1]
			cr = cr1 if nums[2] // nums[1] == nums[1] // nums[0] else 1
		if cd != 0 and cr == 1:
			nt = nums[2] + cd
			result = 'AP'
		elif cd == 0 and cr != 1:
			nt = nums[2] * cr
			result = 'GP'''
		if nums[1] * 2 == nums[0] + nums[2]:
			print 'AP %d' %(nums[2]+(nums[2] - nums[1]))
		elif 0 not in nums:
			cr = nums[2] / nums[1]
			print 'GP %d' %(nums[2]*cr)
except:
	pass