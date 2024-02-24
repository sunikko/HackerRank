def swap_case(s):
    swap_str = ""

    for chr in s:
        if chr.islower():
            swap_str += chr.upper()
        else:
            swap_str += chr.lower()
          
    # swap_str = ''.join([ch.upper() if ch.islower() else ch.lower() for ch in s])
    
  return swap_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
