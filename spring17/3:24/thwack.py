
# they say use a stack queue??

def maze(grid, ugh, r, c, h):

	lunch = False
	#print("row ", r, " col ", c)

	if(r < len(grid) and c < len(grid[0]) and r >= 0 and c >= 0):

		current = grid[r][c]
		#print("current ", current, " lunch ", lunch)

		if(current is "W"):
			return True
		elif((current is not "A") and int(current) <= h):
			return False

		elif(ugh[r][c] < 2):
			#print("HELLO", ugh[r][c])
			ugh[r][c] = ugh[r][c] + 1

			lunch = lunch or (maze(grid, ugh, r + 1, c, h))
			lunch = lunch or (maze(grid, ugh, r - 1, c, h))
			lunch = lunch or (maze(grid, ugh, r, c + 1, h))
			lunch = lunch or (maze(grid, ugh, r, c - 1, h))

			ugh[r][c] = ugh[r][c] - 1
			return lunch
			
	return False




t = input() # test cases
for _ in range(t):

	rc = raw_input().strip().split(' ')
	row = int(rc[0])
	col = int(rc[1])

	h = input() # height

	grid = [["" for _ in range(col)] for _ in range(row)]
	for i in range(row):
		grid[i] = raw_input().strip().split(' ')

	ugh = [[0 for _ in range(col)] for _ in range(row)]

	startR = 0
	startC = 0
	for r in range(row):
		for c in range(col):
			if(grid[r][c] is "A"):
				startR = r
				startC = c

	lunch = maze(grid, ugh, startR, startC, h)
	if(lunch == True):
		print("LUNCH!")
	else:
		print("THWACK!")



