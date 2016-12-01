INPUT <- (low)
INPUT <- (high)
array <- [1,4,5,8,9,12,18]

BINARY_SEARCH(array,low,high)
    start <- 0
    end <- length of array-1
    middle <- 0

    while start <= end
        middle <- (start+end) / 2
        middle <- int(middle)

        if array[middle] is in  range from low to high+1
            return True
        elif array[middle] > high
            end <-middle - 1
        elif array[middle] < low
            start <- middle + 1
    return False

RESULT <- BINARY_SEARCH(array,low,high)
