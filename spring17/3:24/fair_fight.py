
nm = raw_input().strip().split(' ')
n = int(nm[0]) # friends
m = int(nm[1]) # water ballons
str = raw_input().strip().split(' ')

sum = 0

for i in range(n):
	f = int(str[i])
	sum = sum + (m - f)

print(sum)