numbers = open("euler13.txt", 'r')

summ = 0

for line in numbers:
  summ += int(line.rstrip())

print summ

