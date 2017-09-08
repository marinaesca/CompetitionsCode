
n, q = map(int, raw_input().split())

arr = [0 for _ in range(n)]
m = 0

for x in range(q):
	line = map(int, raw_input().split())
	if(line[0] == 1):
		print(m)
	else:
		x = line[1] - 1
		y = line[2]
		if(arr[x] < y):
			arr[x] = y
		if(y > m):
			m = y
