

for _ in range(input()):
	step = int(input())
	dp = [0 for _ in range(1005)]

	dp[0] = 1
	dp[1] = 2

	for n in range(2, step + 1):
		dp[n] += dp[n-1]
		dp[n] += dp[n-2]

		for m in range(n - 1, -1, -1):
			dp[n] += dp[m]

	print dp[step] % 1000000007
