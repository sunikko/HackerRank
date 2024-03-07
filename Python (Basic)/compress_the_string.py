input_list = input()
pre_num = input_list[0]
count = 1

for i in input_list[1:]:
    if pre_num == i:
        count += 1
    else:
        tuple_num = (count, int(pre_num))
        print(tuple_num, end=" ")
        pre_num = i
        count = 1
        
tuple_num = (count, int(pre_num))
print(tuple_num, end="")
