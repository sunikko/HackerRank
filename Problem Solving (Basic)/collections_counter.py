'''
collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
'''
from collections import Counter


count_of_shoes = input()
shoe_sizes_string = input()
shoe_sizes_list = shoe_sizes_string.split()
shoe_sizes = Counter(shoe_sizes_list)
count_of_customers = int(input())
money_earned = 0

for _ in range(count_of_customers):
    customer_order_string = input()
    customer_order_list = customer_order_string.split()
    if shoe_sizes[customer_order_list[0]] > 0:
        money_earned += int(customer_order_list[1])
        shoe_sizes[customer_order_list[0]] -= 1

print(money_earned)
