# INCOMPLETE

# Enter your code here. Read input from STDIN. Print output to STDOUT


# rangers (max), gear, budget
r, g, d = raw_input().strip().split(' ')
r, g, d = [int(r), int(g), int(d)]

gear = {}
for i in range(g):
    name = raw_input().strip()
    require = raw_input().strip()
    stock = raw_input().strip()
    price = raw_input().strip()
    # key is name, value is a list of info
    # require, stock, price, to buy
    gear[name] = [require, stock, price, 0]

# find out best optimization
    
rangers = 0
# this should be the keyset and then alpahbetized
alphaGear = []
print rangers
for i in alphaGear:
    print i
    print gear[i][3]