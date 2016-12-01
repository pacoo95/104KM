
INPUT <- (n)
'''Psedudocode for a function which checks
    if "n" is a prime number '''
CHECKPRIME(n,i)

    res <- False
    if n < 2
        res <- True

    else
        if n <- 2
            res <- False

        if i < n
            if n % i <- 0
                res <- True
            else
                res <- False
                return checkprime(n,i+1)

    true <- " is not a prime number!"
    false <- " is a prime number!"

    if res
        return n + true
    else
        return n + false
    
CHECKPRIME(20,1)
