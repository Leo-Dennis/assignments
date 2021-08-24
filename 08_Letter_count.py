# Letters Count

dict_letters = {}
sentence = input("Enter a sentence: ")

for i in sentence :
    if i in dict_letters.keys() :
        dict_letters[i] += 1
    else:
        dict_letters[i] = 1
print(dict_letters)