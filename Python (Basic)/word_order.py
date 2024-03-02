num_words = int(input())
words_list = {}

for _ in range(num_words):
    word = input()
    # compare if the word in words_list: add them in the array or count+1
    if word not in words_list.keys():
        words_list[word] = 1
    else:
        words_list[word] += 1

print(len(words_list))
print(*words_list.values())
