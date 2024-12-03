import sys
if(len(sys.argv) < 2):
  print('please put in input')
  exit(-1)
D = open(sys.argv[1]).read().strip()

p1 = 0
p2 = 0
p3 = 0
val = {'A': 0, 'B': 1, 'C': 3, 'D': 5}
def part_1():
  for char in D:
    p1 += val[char]
  print(p1)

def part_2():
  pairs = list()
  for i in range(0, len(D), 2):
    pairs.append(D[i] + D[i+1])

  for pair in pairs: 
    first = pair[0]
    second = pair[1]
    if first == 'x' and second == 'x':
      continue
    if first in 'ABCD' and second in 'ABCD':
      p2 += (val[first] + 1)
      p2 += (val[second] + 1)
    else:
      if first == 'x':
        p2 += val[second]
      if second == 'x':
        p2 += val[first]
  print(p2)
    
def part_3():
  global p3
  triples = list()
  for i in range(0, len(D), 3):
    triples.append(D[i] + D[i+1] + D[i+2])
  for triple in triples:
    x_count = triple.count('x')
    one = triple[0]
    two = triple[1]
    three = triple[2]
    if(x_count == 2):
      for char in triple:
        if char in 'ABCD':
          p3 += val[char]
    elif(x_count == 1):
      for char in triple:
        if char in 'ABCD':
          p3 += (val[char] + 1)
    elif(x_count == 0):
      for char in triple:
        p3 += (val[char] + 2)
  print(p3)



part_3()