def isPalindrome(n): 
  m = str(n)
  
  numLen = len(m)

  for i in range(0,numLen):
    if m[i] != m[-(i+1)]:
      return False

  return True

mult = 0
maxPalind = 0

for i in range(999,100,-1):
  for j in range(999,100,-1):
    mult = i*j
    if isPalindrome(mult) and mult > maxPalind:
      maxPalind = mult

print maxPalind
