"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

#1 000 000
## has to be odd value then
pals = [0,1,2,3,4,5,6,7,8,9]

def create_pals():
  for i in range(2,7):
    x = (10**(i-1))+1 ### odd cause binary
    while x < 10**i:
      if int(str(x)) == int(str(x)[::-1]):
        pals.append(x)
      x += 2 ## kept oddness 

create_pals()

doubles = []
for z in pals:
  t = str(bin(z))[2:]
  if t == t[::-1]:
    doubles.append(z)

print sum(doubles)
