
'''Function which reverses the words in a sentence'''
### Big O Notation Included ###
sentence = input("Please enter a sentence: ")      #1
def reversesentence(sentence):
    if len(sentence) == 0:
        return sentence
    else:
        return reversesentence(sentence[1:]) + [sentence[0]] #n
### When the length of the sentence is 0
### the function calls itself with the length of 1 onwards from the sentence and the first word###
print(reversesentence(sentence.split()))
#Big O = O(n)
