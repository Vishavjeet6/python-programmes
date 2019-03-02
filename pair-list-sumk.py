#find count of pairs that have sum equal to the user's input
# in O(n) time complexity
def getPairsCount(arr,n,sums):
    m = [0]*1000
    for i in range(0,n):
        m[arr[i]] += 1

    twice_count = 0
    for i in range(n):
        twice_count += m[sums-arr[i]]
        if (sums-arr[i]) == arr[i]:
            twice_count -= 1
    return twice_count//2
    
    

arr = list(map(int,input().split(' ')))
n = len(arr)
sums = int(input())
print("Count Of Pairs Is",getPairsCount(arr,n,sums))
