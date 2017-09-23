

l = int(input())
colors = dict()
result = 0

for i in range(l):
    clothes, color = raw_input().split()
    if(color in colors):
    	colors[color] += 1
    else:
    	colors[color] = 1

for key, val in colors.items():
	if(val == 2):
		result += 1

print result
