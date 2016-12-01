''' Program that counts the number of trailing 0s
    in a factorial number. '''

fac = int(input("Please enter a fact number: "))
i=0
count = 0
for i in range(1,fac+1):        #iterates from 1 to the inputted fac num
    while True:                 #another iterator which finishes when the statements is False
        if i%5 == 0:            #checks if i divises by 5 without a remainder
            count = count+1     #count the number of divising (which is the result at the end)
            i = i/5             #and if "i" does divide, this line indicates another division
        else:                   # because for example 25 divises by 5 not only once but twice, thats why
            break               # the second division is necesarry 
print(count)
