import time, subprocess, sys
from datetime import *

def shutdown(total):
	subprocess.call(["shutdown", "/s", "/f", "/t", "10", "/c", "You worked for " + total.split(":")[0] + " hours and "+total.split(":")[1]+" minutes today. Time is up for today! C U Tomorrow!!!!"])
	sys.exit()
	
def main():
	cur = datetime.now().time()
	margin = cur.replace(hour=17, minute=4, second=30, microsecond=0)
	while True:
		cur1 = datetime.now().time()
		if margin <= cur1:
			samp = cur1-cur
			days, seconds = samp.days, samp.seconds
			hours = days*24+seconds//3600
			minutes = (seconds%3600)//60
			seconds = seconds%60
			total = str(hours)+":"+str(minutes)+":"+str(seconds)
			shutdown(total)
		
	
if __name__ == "__main__":
	main()