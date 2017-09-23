# Enter your code here. Read input from STDIN. Print output to STDOUT

shirts = int(raw_input().strip())

for i in range(shirts):
    line = raw_input()
    newLine = line[10:-30]
    print(newLine)