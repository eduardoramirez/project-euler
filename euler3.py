import math

def isPrime(n): 
  r = int(math.sqrt(n)) + 1
  
  for i in range(2,r):
    if n % i == 0:
      return False                       
  return True



n = 600851475143

factors = []

root = int(math.sqrt(n)) + 1

for i in range(3,root,2):
  if n % i == 0:
    factors.append(i)

leng = len(factors)
highestFactor = 2

for i in range(1,leng):
  if(isPrime(factors[-i])):
    highestFactor = factors[-i]
    break

print highestFactor
