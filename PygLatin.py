#Code Academy PygLatin Exercise

print ("Welcome to the Reggie Pig Latin Translator!")
#For Python 'input' replaces 'raw_input'
input("Hit 'Return' and then Enter a word:")
original = input()

#it statement first sets input to letters only
if len(original) > 0 and original.isalpha():
    # if then sets case to lower
    word = original.lower()
    first = word[0]
    pyg = 'ay'
    s = (word)
    new_word = s[1:] + first + pyg
    print ("Here's your name in Pig Latin:")
    print (new_word)
else:
    print ("Empty input or entry contains numbers, please try again")

