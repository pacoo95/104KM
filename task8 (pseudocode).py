INPUT <- (word)

REMOVEVOWELS(word)
    vowels <- ["a","e","i","o","u","A","E","I","O","U"]

    if word = ""
        return word
    if first character is in vowels
        replace that character with ""
        return REMOVEWOELS(word from 1st letter onwards)
    else
        return first character of word and REMOVEVOWELS(from 1st charachter onwards)
    print("Word without vowels = " +REMOVEVOWELS(word))
