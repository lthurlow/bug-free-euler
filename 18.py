import pprint
import sys

## bottom up recursive version.
## for #67, used lookup table, top down, check if value already computed


py = \
"""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def path_print(path):
  for t in path:
    sys.stdout.write("%06d "%t)
  sys.stdout.write("\n")
  sys.stdout.flush()

print py
sq_len = len(py.split())/8

py = py[1:-1]
x = [x.split() for x in py.split("\n")]
for y in x:
  print y

def select(row,val,vsum):
  if len(x[row]) == 1:
    vsum = int(x[row][0])
    return vsum
  elif val == 0:
    return int(x[row][0]) + select(row-1,0,vsum)
  elif val == row:
    return int(x[row][val]) + select(row-1,val-1,vsum)
  else:
    return ( int(x[row][val]) + max(select(row-1,val,vsum),select(row-1,val-1,vsum)) )
    #return max(int(x[row-1][val]),int(x[row-1][val-1]))


paths = [int(y) for y in x[-1]]
path_print(paths)

for j in range(0,15):
  print j,select(14,j,0)

#for i in range(sq_len-1,sq_len-2,-1):
  #for j in range(0,i+1):
    #paths[j] = select(i,j,0)
  #path_print(paths)

"""
def select(row,val):
  if len(x[row]) == 1:
    return int(x[row][0])
  elif val == 0:
    return int(x[row-1][0])
  elif val == row:
    return int(x[row-1][-1])
  else:
    return max(int(x[row-1][val]),int(x[row-1][val-1]))
"""
