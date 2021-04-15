import random

a = int(input('a=:'))
b = int(input('b=:'))
if b>a:
    if a%2 == 0:
        print(random.randrange(a,b, 2))
    else:
        print(random.randrange(a+1,b, 2))
else:
     if b%2 == 0:
         print(random.randrange(b,a, 2))
     else:
        print(random.randrange(b+1,a, 2))