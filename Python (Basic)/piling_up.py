# Bigger number of either side is smaller than previous one
blocks = int(input())

for _ in range(blocks):
    return_val = "Yes"
    count_of_block = int(input())
    items_of_block = list(map(int, input().split()))
    previous_num = max(items_of_block[0], items_of_block[len(items_of_block)-1])
    items_of_block.remove(previous_num)
    len_block = len(items_of_block)
    for i in range(len_block-1):
        compare_num = max(items_of_block[0], items_of_block[len_block-i-1])
        if previous_num < compare_num:
            return_val = "No"
            break
        previous_num = compare_num
        items_of_block.remove(compare_num)
    print(return_val)
