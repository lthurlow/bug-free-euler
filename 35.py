import math
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

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

## could also check if any char have parity to return false
def move(n,x,t):
  l = len(str(x))
  y = str(x)
  z = y[n-1:]+y[0:n-1]
  if prime(int(z)):
    t.append(int(z))
    return True
  else:
    return False

def check(x):
  t = []
  for i in xrange(1,len(str(x))+1):
    if not move(i,x,t):
      return False
  return t

## suppose to shortcut, if there is an even value, skip
## so, +10, +100, +1000, +10000, ....
def pos(x):
  y = [y for y in str(x)]
  for i in range(len(y)-1,0,-1):
    if int(y[i]) % 2 == 0:
      return 10**((len(y)-i)-1)
  return False
  
plist = []

x = 3
while x < 1000000:
  #print x
  h = pos(x)
  if h:
    x += h
  if x not in plist:
    z = check(x)
    if z:
      plist += set(z)
  x += 2

print len(plist)+1
