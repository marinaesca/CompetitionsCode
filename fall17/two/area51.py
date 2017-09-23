import math

result = 0

n = int(input())

for i in range(1, int(math.sqrt(n) + 1)):
	if n % i == 0:
		# clean cut
		result += 1

print result