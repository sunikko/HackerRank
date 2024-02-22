def count_substring(string, sub_string):
    cnt = 0
    i = 0
    while(i<len(string)):
        k = string[i:].find(sub_string)
        if k > -1:
            i += k
            cnt += 1
        i += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
