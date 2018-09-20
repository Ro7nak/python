import math
import cmath

a = complex(input())  # ex- 1+2j
x = a.real
y = a.imag

r = math.sqrt((x**2)+(y**2))
r2 = cmath.polar(a) # will give polor values in array
#print(r)
print(r2[0]) # == print(r)
print(r2[1])
