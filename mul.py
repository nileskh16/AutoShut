import sys
try:
	n = int(raw_input())
	for i in range(0, n):
		num = map(int, raw_input().split(" "))
		l1 = num[0]
		l2 = num[1]
		print l1 * l2
except Exception, err:
	print "Arithmatic excpetion!!! %s."%str(err)