
def function(num : int):
    '''This function takes a number and prints it in decrement, each time a new line'''
    for i in range (num , 0 , -1):
        for j in range (i , 0 , -1):
            print(j , end="")
        print()


function(5)
print(function.__doc__)