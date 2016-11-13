''' function that randomly shuffles
        an array of integers.'''

import random

arr1 = [5,3,8,6,1,9,2,7]                #array with the given values
arr2 = []                               #2nd array where the shuffled values are stored
def shuffle(arr1,arr2):
    
    print(arr1)                       
    while len(arr1) > 0:                      #iterates over the lenght of the array while it is bigger than 0
        i=0
        n=0
        n = random.randint(0, (len(arr1)-1))  #picks a random number from array 1
        arr2.append(arr1[n])                  #stores the number from arr1 to arr2 which was randomly picked up
        del arr1[n]                           #deletes the number from arr1 which is already stored in arr2
    print(arr2)

shuffle(arr1,arr2)

#I have made this simple function as I couldn't come up with
#another idea of its creation.
