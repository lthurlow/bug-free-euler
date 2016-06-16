
"""
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors 
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
number.

A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
"""

MAX = 28123

## naive approach without using algerbra
factors = [0 for i in range(0,MAX+1)]

quick = []
abund = []

def find_factor(i):
  fact = [1]
  for x in xrange(2,i):
    if i % x == 0:
      fact.append(x)
  return fact

for i in xrange(1,MAX+1):
  for j in quick:
    if i % j == 0:
      abund.append(i)
      break
  if i not in abund:
    factors[i] = find_factor(i)
    if sum(factors[i]) > i:
      quick.append(i)


allval = [i for i in range(0,MAX+1)]
allabun = set(quick+abund)

allsums = []
for i in allabun:
  for j in allabun:
    allsums.append(i+j)

z = set(allval) - set(allsums)
print sum(z)
