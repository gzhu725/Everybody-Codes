# creds: jonathan paulson (i got too lazy for part 3... oops)
import sys
from collections import Counter
D = open(sys.argv[1]).read().strip()
D = D.split('\n')
D = [[c for c in row] for row in D]
R = 8
C = 8

count = 0
while True:
    changed = False
    for br in range(0, len(D), 6):
        if br+R-1>=len(D):
            continue
        for bc in range(0, len(D[br]), 6):
            if bc+C-1>=len(D[br]):
                continue

            count += 1

            block = ''
            G = [[D[br+r][bc+c] for c in range(C)] for r in range(R)]
            i = 0
            for r in range(R):
                for c in range(C):
                    if G[r][c] == '.':
                        row = {G[r][cc] for cc in range(C)}
                        col = {G[rr][c] for rr in range(R)}
                        final = row & col
                        final.discard('.')
                        final.discard('?')
                        i += 1
                        if len(final) == 1:
                            ch = list(final)[0]
                            D[br+r][bc+c] = ch
                            changed = True
            for r in range(R):
                for c in range(C):
                    if G[r][c] == '?':
                        row = {G[r][cc] for cc in range(C)}
                        col = {G[rr][c] for rr in range(R)}
                        if '*' not in row:
                            dots = [cc for cc in range(C) if G[r][cc]=='.']
                            if len(dots) == 1:
                                dot_col = Counter(G[rr][dots[0]] for rr in range(R))
                                opts = [k for k,v in dot_col.items() if v==1 and k!='.']
                                if len(opts) == 1:
                                    D[br+r][bc+c] = list(opts)[0]
                                    changed = True
                        if '*' not in col:
                            dots = [rr for rr in range(R) if G[rr][c]=='.']
                            if len(dots) == 1:
                                dot_row = Counter(G[dots[0]][cc] for cc in range(C))
                                opts = [k for k,v in dot_row.items() if v==1 and k!='.']
                                if len(opts) == 1:
                                    D[br+r][bc+c] = list(opts)[0]
                                    changed = True
    if not changed:
        break

ans = 0
for br in range(0, len(D), 6):
    if br+R-1>=len(D):
        continue
    for bc in range(0, len(D[br]), 6):
        if bc+C-1>=len(D[br]):
            continue
        G = [[D[br+r][bc+c] for c in range(C)] for r in range(R)]
        ok = True
        block_score = 0
        i = 0
        for r in [2,3,4,5]:
            for c in [2,3,4,5]:
                if G[r][c] == '.' or G[r][c]=='?':
                    ok = False
                else:
                    ch_int = ord(G[r][c])-ord('A')+1
                    assert 1<=ch_int<=26
                    i += 1
                    block_score += i*ch_int
        if ok:
            ans += block_score


print(ans)