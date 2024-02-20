import re

input_s = input()
input_k = input()

s = 0
e = 0
while s < len(input_s):
    m = re.search(r'({})'.format(input_k), input_s[s:])
    if m is not None:
        e = m.end() + (s - 1)
        s += m.start()
        print((s,e))
    s += 1
        
if e == 0:
    print((-1, -1))
