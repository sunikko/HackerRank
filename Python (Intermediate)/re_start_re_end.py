import re

input_s = 'aaadaa'
input_k = 'aa'

s = 0
e = 0

for i in range(len(input_s)):
    m = re.search(r'({})'.format(input_k), input_s[s+i:])
    if m is not None:
        s = m.start() + i
        e = m.end() + (i - 1)
        print((s,e))
        
if e == 0:
    print(-1, -1)
