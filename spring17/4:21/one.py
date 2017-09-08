# can just reverse string & count errors (need only 2)

def func (word):
	p1 = 0
	p2 = len(word) - 1
	count = 0
	while(p1 <= p2):
		if(word[p1] != word[p2]):
			count += 1
		p1 += 1
		p2 -= 1
	return count


n = int(input())
st = raw_input()

substrings = set()

for i in range(n):
	for j in range(i + 1, n + 1):
		word = st[i:j]
		if(func(word) == 1):
			substrings.add(word)

print(len(substrings))
