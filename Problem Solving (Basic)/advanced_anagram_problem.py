# Advanced Anagram Problem:
# Write a Python function that takes a list of strings as input 
# and groups together strings that are anagrams of each other. 
# The function should return a list of lists, 
# where each inner list contains strings that are anagrams of each other.

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False
    
# if it is str in str_dict
# return str_dict.key
# else False
def key_anagram_in_dict(str, str_dict):
    for str_item in str_dict.keys():
        if is_anagram(str, str_item):
            return str_item
    return False

def group_anagrams(strs):
    # put them in a dict in a value group like {'eat':['eat', 'tea','ate'], 'tan':['tan','nat']..}
    # append it if is_anagram(str, dict[key])
    # return the dict to list
    group_anagrams_dict = {}
    for str in strs:
        anagram_key = key_anagram_in_dict(str, group_anagrams_dict)
        if anagram_key:
            group_anagrams_dict[anagram_key].append(str)
        else:
            group_anagrams_dict[str] = [str]
    return list(group_anagrams_dict.values())


# Test the function
test_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(test_strings)
print(result)
# expectation return [["eat", "tea", "ate"], ["tan", "nat"], ["bat"] ]
