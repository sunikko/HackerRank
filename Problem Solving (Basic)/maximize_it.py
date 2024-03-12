lines, m = map(int, input().split())
max_s = 0
for _ in range(lines):
    numbers = list(map(int, input().split()))
    max_num = max(numbers)
    max_s += max_num**2
max_s %= m
print(max_s)
