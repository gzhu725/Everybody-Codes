import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
D = D.split('\n')
grid = list()
for line in D:
  grid.append(list(line))
p1 = ''
rows = len(grid)
cols = len(grid[0])
for r in range(rows):
  for c in range(cols):
    if grid[r][c] == '.':
      row_letters = set(grid[r][0:2] + grid[r][6:8])
      col_letters = set([grid[i][c] for i in [0,1,6,7]])
      l = (tuple(row_letters.intersection(col_letters))[0])
      p1 += l

print(p1)

p2 = 0
for i in range(len(p1)):
  p2 += (i + 1) * (ord(p1[i]) - 64)
print(p2)