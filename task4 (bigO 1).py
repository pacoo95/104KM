#Big O notation

import random

arr1 = [5,3,8,6,1,9,2,7]                #1   
print(arr1)                             #1
arr2 = []                               #1       
while len(arr1) > 0:                    #n                
    i=0                                 #n
    n=0                                 #n
    n = random.randint(0, (len(arr1)-1))#n
    arr2.append(arr1[n])                #n 
    del arr1[n]                         #n
print(arr2)                             #1

#O(6n+4) = O(n)
