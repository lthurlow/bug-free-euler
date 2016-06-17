import math

"""
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula as discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients,

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

MIN = -1001
MAX = 1001


## stack overflow like a boss
def prime(n):
  if (n < 2):
    return False
  elif (n == 2 or n == 3):
    return True
  elif (n%2 == 0 or n%3 == 0) :
    return False
  else:
    sqrtN = math.sqrt(n)+1;
    i = 6
    while i <= sqrtN:
      if (n%(i-1) == 0 or n%(i+1) == 0):
        return False
      i += 6
  return True


prim_l = []
for i in range(0,1001):
  if prime(i):
    prim_l.append(i)
    prim_l.append(-1*i)

prim_l = sorted(prim_l)

max_prime = 10
coeff = [0,0]

def fun(a,b):
  for w in range(0,5*MAX):
    if not prime(abs((w**2)+(w*x)+b)):
      return w

for x in range(MAX,MIN,-1):
  if x % 2 == 1:
    for y in prim_l:
      t = fun(x,y)
      if t > max_prime:
        max_prime = t
        coeff[0] = x
        coeff[1] = y
        #print "%d,%d: %d" % (x,y,t)

print coeff[0]*coeff[1]
