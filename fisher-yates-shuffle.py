import random
#fisher yates shuffle

def randomize(arr,n):
    
    for i in range(n-1,0,-1):
        j = random.randint(0,i)
        arr[i],arr[j] = arr[j],arr[i]
    return arr

t = int(input("Enter Testcases : "))
for i in range(t):
    arr = list(map(int,input("Enter array : ").split(' ')))
    n = len(arr)
    print(randomize(arr,n))
