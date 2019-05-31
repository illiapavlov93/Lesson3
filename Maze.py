import queue

labyrint = ['111111111111111111',
            '1x0010000000000001',
            '111011101111111101',
            '101010000100000001',
            '101011010101111111',
            '101000010100001001',
            '100011110101111101',
            '101110010100000001',
            '100000000101101111',
            '101101111100100001',
            '101001000000101001',
            '101101111111101001',
            '101000000000001001',
            '101011110100101001',
            '101000010111111001',
            '111011110100000001',
            '101000000101111111',
            '101011110101010101',
            '1000000101000000#1',
            '111111111111111111']

i = 0
for line in labyrint:
    if 'x' in line:
        column = line.index('x')
        startpoint = (i, column)
    if '#' in line:
        column = line.index('#')
        finishpoint = (i, column)
    i += 1

was = {}
q = queue.Queue()
q.put(startpoint)
was[startpoint] = None

while q:
    current = q.get()
    if current == finishpoint:
        break
    if labyrint[current[0] - 1][current[1]] != '1':
        if (current[0] - 1, current[1]) not in was.keys():
            was[(current[0] - 1, current[1])] = current
            q.put((current[0] - 1, current[1]))
    if labyrint[current[0]][current[1] - 1] != '1':
        if (current[0], current[1] - 1) not in was.keys():
            was[(current[0], current[1] - 1)] = current
            q.put((current[0], current[1] - 1))
    if labyrint[current[0] + 1][current[1]] != '1':
        if (current[0] + 1, current[1]) not in was.keys():
            was[(current[0] + 1, current[1])] = current
            q.put((current[0] + 1, current[1]))
    if labyrint[current[0]][current[1] + 1] != '1':
        if (current[0], current[1] + 1) not in was.keys():
            was[(current[0], current[1] + 1)] = current
            q.put((current[0], current[1] + 1))

way = [finishpoint]
while was[finishpoint] is not None:
    way.append(was[finishpoint])
    finishpoint = was[finishpoint]
print('way', way[::-1])
