pyg = 'ay'
original = raw_input('Enter a word:')
if str(original) > 0 and original.isalpha():
    first = original[0]
    original = original.lower()
    word = original
    new_word = word + pyg
    if first == "u" or first == "i" or first == "e" or first == "a" or first == "o":
        print(new_word)
    else:
        new_word = original[1:] + original[0:1] + pyg
        print(new_word)
else:
    print 'Error. Try again.'
