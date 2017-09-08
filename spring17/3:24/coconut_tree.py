

setUp = raw_input().strip().split(' ')
n = long(setUp[0]) # num tress
v = int(setUp[1]) # value coconut
t = long(setUp[2]) # max trees

probs = [0.0 for _ in range(n)]

for i in range(n):
	tree = raw_input().strip().split(' ')
	p = int(tree[0]) # penalty
	c = int(tree[1]) # num coconuts in tree
	f = int(tree[2]) # chance fall

	# how does probability work
	percent = float((f / 100.0))
	lose = float(p * percent)
	win = float((c * v) * (1 - percent))
	if(f == 100):
		prob = 0 - lose
	else:
		prob = win - lose

	probs[i] = prob
	#print("p c f ", p, c, f, "win ", win, " lose ", lose, " prob", prob)

probs = sorted(probs, key=float)
total = 0
trees = t
index = len(probs) - 1

# sliding window thing 
while(index >= 0 and trees > 0):
	if(probs[index] > 0):
		total = total + probs[index]
		trees = trees - 1
	index = index - 1


print(probs)
print(total)


