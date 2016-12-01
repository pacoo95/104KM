
array = [1,4,5,8,9,12,18]
print(array)
low = int(input("Enter low: "))
high = int(input("Enter high: "))

'''BINARY SEARCH ALGORITHM ADAPTED TO SEARCH IN
    INTERVAL, NOT FOR A SPECIFIC VALUE'''

def binary_search(array,low, high):
    start = 0
    end = len(array)-1
    middle = 0
    while start <= end:
        middle = (start+end)/2
        middle = int(middle)
        if array[middle] in range (low, high+1):
            return True
        elif array[middle] > high:
            end = middle - 1
        elif array[middle] < low:
            start = middle + 1
    return False
    
print(binary_search(array,low,high))

# Big O = log n
