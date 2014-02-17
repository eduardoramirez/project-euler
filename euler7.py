import math

def isPrime(n): 
  if n % 2 == 0:
    return False

  r = int(math.sqrt(n)) + 1
  
  for i in range(3,r,2):
    if n % i == 0:
      return False                       
  return True


i = 3
primeCount = 1

while True: 
  if(isPrime(i)):
    primeCount += 1

  if primeCount == 10001:
    break

  i += 2

print i
