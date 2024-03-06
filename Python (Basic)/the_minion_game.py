# input: String banana
# print: winner and score
def minion_game(string):
    # ===== 1 ======
    # make two dict {word:score}
    # sub for loop b/ba/ban/bana/banan/banana, a/na/ana/anan/anana, .... 
    # then sum of dict.values()
    
    # ===== 2 ======
    # but actually, it means each count is len(string)
    # so instead of saving in a actual dict , save just length
    consonants_len = 0
    vowels_len = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    
    for x in range(len(string)):
        sub_chr = string[x:x+1].lower()
        if sub_chr[0:1] in vowels_list:
            vowels_len += len(string) - x
        else:
            consonants_len += len(string) - x
            
    
    if vowels_len > consonants_len:
        print("Kevin", vowels_len)
    elif vowels_len == consonants_len:
        print("Draw")
    else:
        print("Stuart", consonants_len)
        
    '''
    consonants_dict = {}
    vowels_dict = {}
    
    for x in range(len(string)):
        for y in range(1, len(string[x:]) + 1):
            sub_chr = string[x:x+y].lower()
            if sub_chr[0:1] in vowels_list:
                vowels_dict[sub_chr] = vowels_dict.get(sub_chr, 0) + 1
            else:
                consonants_dict[sub_chr] = consonants_dict.get(sub_chr, 0) + 1
    print(vowels_dict, consonants_dict)
    print(sum(vowels_dict.values()), sum(consonants_dict.values()))
    
    sum_vowels = sum(vowels_dict.values())
    sum_consonants = sum(consonants_dict.values())
    if sum_vowels > sum_consonants:
        print("Kevin", sum_vowels)
    elif sum_vowels == sum_consonants:
        print("Draw")
    else:
        print("Stuart", sum_consonants)
    '''
        
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
