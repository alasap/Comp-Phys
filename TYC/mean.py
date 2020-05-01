def mean(val):
    num=0
    for i in range(0,len(val)):
        num += val[i]
    ans= num/ len(val)
    return ans

mean([0,1,2,3])

