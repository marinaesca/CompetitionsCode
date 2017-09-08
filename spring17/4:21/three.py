
# input:
# 2
# 4 2
# 1 2
# 3 4
# 4 6
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4


q = int(input())

for _ in range(q):

	#n vertices, m edges
	ver, edge = map(int, raw_input().split())
	arr = [[0 for _ in range(ver)] for _ in range(ver)]

	for m in range(edge):
		i, j = map(lambda x: int(x) - 1, raw_input().split())
		arr[i][j] += 1
		arr[j][i] += 1
		
	print("\n".join(map(str, arr)))
	# adj matrix created - done

	v1 = []
	v2 = []

	vertexsafe = True
	for vertex in range(ver):
		index1 = 0
		index2 = 0
		while(index1 < len(v1) and index2 < len(v2) and vertexsafe):
			# if you have a neighbor in both v's BAD
			if(arr[vertex][v1[index1]] == 1 and arr[vertex][v2[index2]] == 1):
				vertexsafe = False
			elif(arr[vertex][v1[index1]] == 1):
				v2.append(vertex)
			else:
				v1.append(vertex)
			index1 += 1
			index2 += 1

	if vertexsafe:
		print("YES")
	else:
		print("NO")

