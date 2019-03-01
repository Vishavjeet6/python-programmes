a=list(map(int,input().split(' ')))
max_ending_here = 0
max_so_far = 0
for i in a:
    max_ending_here = max_ending_here + i
    if max_ending_here<0:
        max_ending_here = 0
    if max_so_far<max_ending_here:
        max_so_far = max_ending_here
        
