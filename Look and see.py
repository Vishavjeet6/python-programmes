a=input()
g=""
i=0
while i<len(a):
    c=0
    for j in range(i,len(a)):
        
        if a[i]==a[j]:
            c=c+1
        else:
            break
    g=g+str(c)+a[i]
    i=i+c
print(g)   
    
