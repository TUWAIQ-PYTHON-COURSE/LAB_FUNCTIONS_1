#[1]
'''
def shape(num:int):
  #  x =""
    for i in range(num ,1,-1):
        for j in range (0,i):
            print(num, end=' ')
    print("\r")


shape(5)
'''



def shape(num:int):
    for i in range(0, num + 1):
        for j in range(num - i, 0, -1):
             print(j, end=' ')
        print()

shape(5)
'''
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()
'''