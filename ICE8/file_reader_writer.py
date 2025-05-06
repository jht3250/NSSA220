import sys

f = open(sys.argv[1], 'r')
out = open('new_iris.txt', 'w')

line = ''

while True:
    line = f.readline().strip()
    if (line == ''):
        break
    print(line)
    active = line.split(',')
    for i in range(4):
        num = float(active[i])
        active[i] = str(num*2) + ','
    active[4] = active[4] + '\n'
    out.write(''.join(active))
    
f.close()
out.close()