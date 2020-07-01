#This translates the input into giraffe language
#Giraffe language is the same word with the vowels replaced by gs
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation +"G"
            else:
                translation = translation +"g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase:")))