# pig latin
# if a word starts with a vowel add "ay" to end
# if a word does not start with a vowel, put first letter at end , and then add 'ay'
# eg : word --> ordway
# eg : apple --> appleay
import os

os.system('cls')

def pig_latin(word):
    '''
    DOCSTRING: For fun
    '''
    first_letter = word[0]
    # check if wovel
    if first_letter.lower() in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'
    
    return pig_word

print(pig_latin('word'))
help(pig_latin)