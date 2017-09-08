

for _ in range(input()):

	h, d, w, n = map(int, raw_input().split())
	print (h * d * (12 * w)) * n * (n + 1) / 2
