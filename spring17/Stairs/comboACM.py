
def getStep(cur):
	global count

	if(cur == 0):
		count += 1
		return
	else :
		getStep(cur - 1)
		if(cur > 1):
			getStep(cur - 2)
		for n in range(cur - 1, -1, -1):
			getStep(n)



for _ in range(input()):
	count = 0
	getStep(int(input()))
	print count
