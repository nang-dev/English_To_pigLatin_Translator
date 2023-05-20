# suffix - constant
pyg = 'ay'

# No clue
def convert(original: str):
    first = original[0]
    original = original.lower()
    word = original
    new_word = word + pyg
    if first == "u" or first == "i" or first == "e" or first == "a" or first == "o":
        return new_word
    else:
        new_word = original[1:] + original[0:1] + pyg
        return new_word


def main():
    user_input = input("Enter a sentance:")
    
    # Remove characters that might mess this up
    user_input = user_input.replace(",", "")
    user_input = user_input.replace(".", "")
    user_input = user_input.replace("?", "")
    user_input = user_input.replace("!", "")
    
    # Check if text is ok
    if not user_input.isalpha:
        print("The string you entered is invalid!")
        return
    
    # Split text up
    user_input = user_input.split(" ")
    
    # Run the translation
    for i in user_input:
        print(convert(i),end=" ")

if __name__ == "__main__":
    main()

