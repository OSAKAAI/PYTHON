def wordc(s):
    word_list = s.split()
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

s = input("Enter a sentence: ")
word_frequency = wordc(s)
print("Word frequency:", word_frequency)
