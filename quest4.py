import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()
D = list(map(int, D.split('\n')))
short = min(D)
p1 = 0
for n in D:
  if n != short:
    p1 += abs(n-short)
print(p1) # this is also p2 lol

# onto part 3
D.sort()
p3 = float('inf')
for t in D:
  #each target nail
  total = 0
  for n in D:
    #each nail
    total += abs(n - t)
  p3 = min(p3, total)
print(p3)