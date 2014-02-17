'''
a = m^2 - n^2 
b = 2mn
c = m^2 + n^2

a + b + c = 1000

m^4 + 2(m*n) = 1000

for m > n
'''

import math

n = 1
m = 2
temp = 0

while True:
  while True:
    temp = 2*pow(m,2) + 2*(m*n)
    
    if temp == 1000:
      break
    elif temp > 1000:
      break

    m += 1

  if temp == 1000:
    break

  m = n + 1
  n += 1

a = pow(m,2) - pow(n,2)
b = 2*m*n
c = pow(m,2) + pow(n,2)

print a*b*c
