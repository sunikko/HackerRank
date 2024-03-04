# Write a function that takes a string as input and
# returns the count of vowels (a, e, i, o, u) in the string.
# input : a string
# return : int
def count_of_vowels(str):
    vowels_list = (‘a’, ‘e’, ‘i’, ‘o’, ‘u’)
    count_vowels = 0
    for chr in str:
        chr = chr.lower()
        if chr in vowels_list:
            count_vowels += 1
    return count_vowels

str = “WrIte”;
print(count_of_vowels(str))
