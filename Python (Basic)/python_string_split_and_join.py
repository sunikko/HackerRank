def split_and_join(line):
    str_list = line.split(" ")
    str_list = "-".join(str_list)
    return str_list

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
