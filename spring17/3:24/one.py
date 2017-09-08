# long hike

n = input()
str = raw_input().strip().split(' ')
sum = 0

for i in range(n):
	t = str[i]
	sum = sum + int(t)

print(sum)