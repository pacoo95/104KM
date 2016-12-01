INPUT <- (word)

REVERSEWORD(word)
    if length of word <- 0
        return word
    else
        return reverseword(word[1:])+[word[0]]
    
