import sys
from collections import defaultdict

if len(sys.argv) < 2:
    print('please put in input')
    exit(-1)

D = open(sys.argv[1]).read().strip()
D = D.split('\n')

d = {}
for val in D:
    uh = val.split(':')
    letter, mites = uh[0], uh[1].split(',')
    d[letter] = mites

def solve(n, starting_mite):
    mites = [starting_mite]
    print(mites)
    for _ in range(n):
        new_mites = []
        for mite in mites:
            new_mites.extend(d[mite])
        mites = new_mites
    return len(mites)

#solve(4, 'A') p1
#solve(10, 'Z') p2
by_typ = {}
for typ in d.keys():
    have = {typ: 1}
    for _ in range(20):
        new_have = defaultdict(int)
        for k,v in have.items():
            for x in d[k]:
                new_have[x] += v
        have = new_have
    by_typ[typ] = sum(have.values())

mx = max(by_typ.values())
mn = min(by_typ.values())
print(mx-mn) #p3