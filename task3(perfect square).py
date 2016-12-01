

integer = int(input("Please enter an integer: "))
def perfectsquare(integer):
    '''A function which returns the highest perfect square which is less
    or equal to its parameter (a positive integer).'''
    i = 1
    while True:             #iterates while the condition is True
        if i*i > integer:   #checks if i multiplied by itself is higher than the input
            break
        i +=1               #if i multiplied by itslef isn't higher than the input increases i

    i = i - 1
    print(i*i)
perfectsquare(integer)
