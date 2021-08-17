punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~ """
sentence = input("Enter a sentence to check whether it is palindrome or not: ")

for character in punctuations :
    sentence = sentence.replace(character, "")
    
reversed_sentence = sentence[::-1]    

if sentence == reversed_sentence :
    print(f'"{sentence} is a palindrome"')
else :
    print(f'"{sentence} is not a palindrome"')