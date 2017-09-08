

for _ in range(input()):
	step = int(input())
	total = [0 for _ in range(step + 2)]
	loop = [0 for _ in range(step + 2)]

	#loopI1 = 0
	#totalI1 = 0
	#loopI = 0
	#totalI2 = 0

	loop[0] = 0
	loop[1] = 1
	total[0] = 1
	total[1] = 2

	for i in range(2, step + 1):
		loop[i] = loop[i-1] + total[i-1]
		total[i] = loop[i] + total[i-1] + total[i-2]
		loop[i] = loop[i] % 1000000007
		total[i] = total[i] % 1000000007

	print total[step] % 1000000007
