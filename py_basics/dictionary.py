data_path = "py_basics/rosalind_ini6.txt"

string = open(data_path, 'r').read().split()
dict_words = {}

for word in string:
    if word in dict_words: 
        dict_words[word] += 1
    else: 
        dict_words[word] = 1

for word in dict_words: 
    print(word, dict_words[word])
