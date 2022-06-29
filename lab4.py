# Create a function that takes 1 parameter of type int 
#then it prints out the result formatted like the following patter (if we give it 5 for example):

def fun_one_parameter(p1 : int ):
 '''Document the newly created function'''
 for x in range(p1,0,-1):
    for y in range(x,0,-1):
        print(y,end=" ")
    print()
fun_one_parameter(5)
print(fun_one_parameter.__doc__)

 

