#  Create a function that takes 1 parameter of type int , then it prints out the result formatted
#  like the following patter (if we give it 5 for example):

'''
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
'''

def one_parameter(number : int):
    '''prints numbers!'''
    for x in range (number, 0, -1):
        for y in range(x, 0,-1):
            print (y, end=" ")
        print ()




### Document the newly created function. describe what it does, then print the documentation. 



one_parameter (5)
print(one_parameter.__doc__)