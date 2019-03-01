import math
n=int(input())
g=[]
s=[]
l=list(map(int,input().split(' ')))
for x in l:
    for y in g:
        if math.gcd(x,y)!=1:
            g.append(x)
            l.remove(x)
    s.append(g)
