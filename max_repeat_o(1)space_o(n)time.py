# max frequency with o(1)space and o(n) time
# condition no two max frequecny only one
# for more than one eg (1,1,2,2)
# check next program
# https://www.geeksforgeeks.org/find-the-maximum-repeating-number-in-ok-time/

l = list(map(int,input("Enter Array : ").split(' ')))

#length
k = len(l)

for i in range(k):
    l[l[i]%k] += k

max_fre = 0
result = 0
for i in range(k):
    if l[i] > max_fre:
        max_fre = l[i]
        result = i

print(result)


# to retrieve array
for x in range(k):
    l[x] = l[x]%k

print(l)
