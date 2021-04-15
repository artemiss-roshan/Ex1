import math

a = int(input('a=:'))
b = int(input('b=:'))
c = int(input('c=:'))

d = b*b-4*a*c

if d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("x ", x)
elif d < 0:
    print ("no answer")
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print ("x1 ", x1, " x2", x2)