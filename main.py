# LAB_FUNCTIONS_1
## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):


def fuunction( m: int ):
  '''Document the newly created function'''
  for i in range(0, m + 1):
    for x in range(m - i, 0, -1):
      print(x, end= " ")
    print()
fuunction(5)


print(fuunction.__doc__)