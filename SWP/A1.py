#SWP-A1
# exercise 2.12
#Program for caclulating all of the prime numbers below a specified limit.
primes=[2]
lim=10000
n=3
while n<lim:
    for i in primes:
        if n%i==0:
            bool='false'
            break
        else:bool='true'
    if bool=='true':
        primes.append(n)
    n=n+1
print(primes)
