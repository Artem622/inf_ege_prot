'''
#одна куча
from functools import lru_cache
def moves(s):
    return s+1,s+4,s*5
@lru_cache(None)
def game(s):
    if s>=68: return 'W'
    if any(game(m) == 'W' for m in moves(s)): return 'P1'
    if any(game(m) == 'P1' for m in moves(s)): return 'B1'
    if any(game(m) == 'B1' for m in moves(s)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(s)): return 'B2'

for s in range(1,68):
    if game(s) is not None:
        print(s,game(s))'''

#после неудачного хода---- any

#две кучи
'''from functools import lru_cache

def moves(h):
    a,b=h
    return (a+1,b),(a,b+1),(a,b*2),(a*2,b)
@lru_cache((None))
def game(h):
    if h[0]<=1 or h[1]<=1:
        return
    if sum(h)>=74:
        return 'Win'
    if any(game(m)=='Win' for m in moves(h)):
        return 'P1'
    if any(game(m)=='P1' for m in moves(h)):
        return 'B1'
    if any(game(m)=='B1' for m in moves(h)):
        return 'P2'
    if all(game(m)=='P1' or game(m)=='P2'for m in moves(h)):
        return 'B2'
for s in range(1,62):
    if  game((12,s)) is not None:
        print(s,game((12,s)))'''
