# issue: some cases - Time limit exceeded or Runtime Error

# input: String banana
# print: winner and score
def minion_game(string):
    # make two dict {word:score} and a vowles list to compare
    # sub for loop b/ba/ban/bana/banan/banana, a/na/ana/anan/anana, ....
    # then sum of dict.values()
    consonants_dict = {}
    vowels_dict = {}
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    for x in range(len(string)):
        for y in range(1, len(string[x:]) + 1):
            sub_chr = string[x:x+y].lower()
            if sub_chr[0:1] in vowels_list:
                vowels_dict[sub_chr] = vowels_dict.get(sub_chr, 0) + 1
            else:
                consonants_dict[sub_chr] = consonants_dict.get(sub_chr, 0) + 1
    # print(vowels_dict, consonants_dict)
    # print(sum(vowels_dict.values()), sum(consonants_dict.values()))
    sum_vowels = sum(vowels_dict.values())
    sum_consonants = sum(consonants_dict.values())
  
    if sum_vowels > sum_consonants:
        print("Kevin", sum_vowels)
    elif sum_vowels == sum_consonants:
        print("Draw")
    else:
        print("Stuart", sum_consonants)
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
