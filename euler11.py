grid = [[0 for x in xrange(20)] for x in xrange(20)]

numbers = open("euler11.txt",'r')

maxMult = 0

r = 0
c = 0

for line in numbers:
  row = line.rstrip().split(' ')
  row = map(int,row)
  
  for num in row:
    grid[r][c] = num
    c += 1

  r += 1
  c = 0

# in a row 
for r in range(0,20):
  for c in range(0,20-3):
    temp = grid[r][c] * grid[r][c+1] * grid[r][c+2] * grid[r][c+3]
    
    if temp > maxMult:
      maxMult = temp

# in columns
for r in range(0,20-3):
  for c in range(0,20):
    temp = grid[r][c] * grid[r+1][c] * grid[r+2][c] * grid[r+3][c]

    if temp > maxMult:
      maxMult = temp

# in crosses
for r in range(3,20-3):
  for c in range(3,20-3):
    temp = grid[r-3][c-3] * grid[r-2][c-2] * grid[r-1][c-1] * grid[r][c]
    
    if temp > maxMult:
      maxMult = temp

    temp = grid[r][c-3] * grid[r-1][c-2] * grid[r-2][c-1] * grid[r-3][c]

    if temp > maxMult:
      maxMult = temp

print maxMult
