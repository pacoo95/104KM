#Big O Notation

fac = int(input("Please enter a fact number: ")) #1
i=0                                              #1
count = 0                                        #1
for i in range(1,fac+1):                         #n   
    while True:                                  #n*n   
        if i%5 == 0:                             #n*n
            count = count+1                      #n*n   
            i = i/5                              #nlogn
        else:                                    #n*n   
            break                                #n*n   
print(count)                                     #1

#O(n+6n^2+4) = O(n*nlogn)
