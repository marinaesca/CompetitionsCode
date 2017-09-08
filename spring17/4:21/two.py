#problem is when stones inc may need to add more twos possibilities


# num, player
def func(n, player):
	print("n ", n, " player ", player)
	if(player % 2 == 1 and n == 0):
		# then it is odd's turn but already zero
		return True
	elif(n <= 0):
		return False

	count = 0
	k = 1
	while(k <= n):
		print("k ", k)
		if func(n - k, player + 1):
				return True	
		count += 1
		k = pow(2, count)
	return False

def createTwos(num):
	twos = []
	count = 0
	k = 1
	while(k <= n):
		count += 1
		k = pow(2, count)
		twos.append(k)
	#reverse twos
	return twos[::-1]


t = int(input())

for i in range(t):
	num = int(input())
	stones = 0
	twos = createTwos(num)
	while(not func(num + stones, 0)):
		print("add a stone")
		stones += 1
	print(stones)




