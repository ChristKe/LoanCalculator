import math

x = int(input())
base = int(input())

# if x < 0:
#    x = abs(x)
if base == 0 or base == 1 or base < 0:
    n_log = math.log(x)
    print(round(n_log, 2))
else:
    res = math.log(x, base)
    print(round(res, 2))
