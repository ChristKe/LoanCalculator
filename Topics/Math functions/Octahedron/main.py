import math
edge_le = int(input())
area = 2 * (math.sqrt(3)) * (math.pow(edge_le, 2))
volume = ((1 / 3) * (math.sqrt(2)) * (math.pow(edge_le, 3)))
print(round(area, 2), (round(volume, 2)))
