# -- coding: utf-8 --
import math
 
x = -2.235 * (10**-2)
y = 2.23
z = 15.221
s = ((math.e ** (math.fabs(x-y)) * math.fabs(x - y) ** x + y) / ((math.atan(1/x)) + (math.atan(1/z))) + (x**6 + math.log(y)**2) ** (1/3))
 
 
 
print (s)