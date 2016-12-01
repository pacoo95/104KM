
word = input("Please enter a word: ")

def removevowels(word):
    '''Function which removes VOWELS
     from a word! '''
    vowels = ["a","e","i","o","u","A","E","I","O","U"]

    if word == "":
        return word
    
    if word[0] in vowels:       #if 1st letter is a vowel
        word.replace(word[0],"") # replace it with an empty string
        return removevowels(word[1:]) # and call the function from the 2nd letter onwards
    else:
        return word[0]+removevowels(word[1:]) # otherwise we call the function again but from the next letter

print("Word without vowels = " + removevowels(word))
