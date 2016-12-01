n = int(input("Number: "))
def checkprime(n,i):
''' Function which checks
    if "n" is a prime number '''   
    res = False
    if n < 2:
        res = True
        
    else:
        if n == 2:
            res = False
            
        if i<n:
            if (n % i) == 0:
                res = True
                
            else:
                res = False
                return checkprime(n,i+1)
    true = " is not a prime number!"
    false = " is a prime number!"
    if res:
        return str(n) + true
    else:
        return str(n) + false
        
print(checkprime(n,2))

