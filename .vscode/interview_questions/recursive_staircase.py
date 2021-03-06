
#number of ways to traverse a n number of stairs.
def n_ways(stairs):
    if stairs==0 or stairs==1:
        return 1
    return n_ways(stairs-1)+n_ways(stairs-2)


#with bottom approach
def n_ways_dp(s):
    if s==0 or s ==1:
        return 1
    num=[1,1]
    for i in range(2,s+1):
        num.append(num[i-1]+num[i-2])
    return num[s]

