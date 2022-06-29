
def following_patter(num:int):
   '''This function takes a number and prints it sequentially in a hierarchical form''' 
   for x in range(num,0,-1):
    for y in range(x,0,-1):
        print (y,end=" ")
    print()

following_patter(5)   
print(following_patter.__doc__) 