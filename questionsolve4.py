4.Write a program that asks the user to enter three numbers and determines which one is the biggest.


a = 10
b = 14
c = 12
def maximum(a, b, c): 

    if (a >= b) and (a >= c): 
        largest = a 

    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
        
    return largest 


print(maximum(a, b, c))
