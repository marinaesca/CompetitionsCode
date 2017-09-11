# INCOMPLETE--


# Enter your code here. Read input from STDIN. Print output to STDOUT

# petal(list), num(list), current, petal index, current bouquet

# this is a terrible way but I'm trying to be fast
# note to self research GCD algos
def checkGCD(petals):
    # first we get the max
    max = petals[0]
    for i in petals:
        if i > max:
            max = i
    
    for i in range(2, max):
        bool = True
        for j in petals:
            # if it's not divisible - bool is false
            if(petals[j] % j != 0):
                bool = False
        if bool:
            return True
    return False

def recurseHer(petal, num, current, index, currentBouquet):
    # base case
    if index == len(petal):
        return currentBouquet
    # so check if all current PAIRS petal nums have a good GDC
    print "this is recursion method: ",current
    current.append(petal[index])
    if(checkGCD(current)):
        currentBouquet += petal[index] * num[index]
        index += 1
        recurseHer(petal, num, current, index, currentBouquet)
    # backtrack
    current = current[:-1]
        
f = int(raw_input().strip())
petal = []
num = []
# set up the creation of the lists
for i in xrange(f):
    # petals, num flowers
    p, s = raw_input().strip().split(' ')
    petal.append(int(p))
    num.append(int(s))
    
# so i want to pair all flower combos and check that the petals make a legit GCD
# do recursion!

# petal(list), num(list), current petals, petal index, current bouquet
current = []
print recurseHer(petal, num, current, 0, 0)    

