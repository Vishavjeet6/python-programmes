def fibinarry(n):
    pl = 0
    while n:
        if n&1 and pl:
            return False
        pl = n&1 
        n>>=1
    return True
k=int(input())
n=0
l=[]
while len(l)<=k:
    if fibinarry(n):
        l.append(n)
    n+=1
print(l[k])
