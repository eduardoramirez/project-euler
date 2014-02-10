a = 1
b = 2
c = 0
evenSum = 0

while a <= 4000000:
  c = a
  a = b
  b = a + c

  if a % 2 == 0:
    evenSum = evenSum + a

print evenSum
