#removing duplicate from string
t = int(input())
MAX=256
for i in range(t):
    s=input("Enter String :")
    g=""
    count=[0]*MAX
    for i in s:
        if count[ord(i)] != 1:
            g += i
            (count[ord(i)]) += 1
    print(g)
        
    
