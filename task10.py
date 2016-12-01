array = [1,2,3,8,1,5,6,7,8,1,2,3,7,9,11,0,1]    #our array with the values
countlist = []                                  #empty list where the count of the ascending values is going to be stored
def extract(array,countlist):
    '''Function which extracts the sub-sequence
    of maximum length which is in ascending order'''
    count = 1
    for i in range(len(array)-1):           #an for loop which goes through the entire array
        if array[i] < array[i+1]:           #if the value is lower than the one next to it
            count = count +1                # increases the counter with 1
        else:
            countlist.append(count)         # otherwise (when the ascending order finishes, append the count number to the count list
            count = 1                       #and set the coutner to 1 again, so we can count the next ascending order
            
    countlist.append(count)                 
    print(countlist)
    print("Maximum length: " + str(max(countlist)))
    maxnum = countlist.index(max(countlist))
    maxn = max(countlist)
    sumL = 0
    for i in range(0,maxnum):               #another for loop which goes from 0 to the index of the highest counter value
        sumL = sumL + countlist[i]          # sum it so we can find where in the first array it is 
    return("Sub-sequence: " +str((array)[sumL:sumL+maxn]))      # return the sub-sequence from the position we found to the position of values where the highest element finishes

print(extract(array,countlist))



