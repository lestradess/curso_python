from functools import reduce

lista =[1,2,3,4,5,6,7,8,9]

impares = filter(lambda x: x%2 !=0 ,lista )

print(reduce (lambda x,y:x+y,impares))