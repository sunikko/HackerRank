def merge_the_tools(string, k):
    # for loop len(string)/k 
    for i in range(0, len(string), k):
        # get k length of string -> set?
        u = ""
        for ch in string[i:i+k]:
            if ch not in u:
                u += ch
        print(u)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
