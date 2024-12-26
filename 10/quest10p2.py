import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
D = D.split('\n')

p2 = 0
for br in range(0, len(D), 9):
  for bc in range(0, len(D[br]), 9):
    grid = [[D[br+j][bc+i] for i in range(8)] for j in range(8)]
    p1 = ""
    for r in range(8):
      for c in range(8):
        if grid[r][c] == '.':
          row_letters = set(grid[r][0:2] + grid[r][6:8])
          col_letters = set([grid[i][c] for i in [0,1,6,7]])
          l = (tuple(row_letters.intersection(col_letters))[0])
          p1 += l

    for i in range(len(p1)):
      p2 += (i + 1) * (ord(p1[i]) - 64)
print(p2)