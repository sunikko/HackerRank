import re

input_s = input()
input_k = input()

s = 0
e = 0
idx = 0
while idx < len(input_s):
    m = re.search(r'({})'.format(input_k), input_s[s:])
    if m is not None:
        # print('start:',m.start(), ', end:', m.end())
        s = m.start() + idx
        e = m.end() + (idx - 1)
        print((s,e))
    s += 1
    idx = s
        
if e == 0:
    print((-1, -1))
