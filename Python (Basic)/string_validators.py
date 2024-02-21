if __name__ == '__main__':
    s = input()
    # In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    print([char_item for char_item in s if char_item.isalnum()] != [])
    
    # In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    print([char_item for char_item in s if char_item.isalpha()] != [])
    
    # In the third line, print True if  has any digits. Otherwise, print False.
    print([char_item for char_item in s if char_item.isdigit()] != [])
    
    # In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    print([char_item for char_item in s if char_item.islower()] != [])
    
    # In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    print([char_item for char_item in s if char_item.isupper()] != [])
    
    # what others did - any([str.isalnum(i) for i in s]))
