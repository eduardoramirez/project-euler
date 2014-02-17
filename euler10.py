import math

def isPrime(n): 
  if n % 2 == 0:
    return False
  
  r = int(math.sqrt(n)) + 1
  
  for i in range(3,r,2):
    if n % i == 0:
      return False                       
  return True


limit = 2000000

primeSum = 2

for i in range(3,limit,2):
  if(isPrime(i)):
    primeSum += i

print primeSum 

