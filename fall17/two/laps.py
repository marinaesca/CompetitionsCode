for _ in range(int(input())):
	lap = dict()
	winners = []
	n, l = map(int, raw_input().split())
	for _ in range(n):
		name = raw_input()
		lap[name] = lap.get(name, 0) + 1
		if lap[name] == l:
			winners.append(name)
	if len(winners) < 2:
		print "Armageddon"
	else:
		print winners[0]
		print winners[1]
