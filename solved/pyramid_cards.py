t = input()
for i in range(0, t):
	n = input()
	total = (n * (n + 1)) + (n * (n-1))/2
	print total%1000007