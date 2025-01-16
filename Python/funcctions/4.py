import math
def area_C(r):
  area = round(math.pi*r*r,2)
  circum = round(2*math.pi*r,2)
  return area,circum
print(area_C(2.5))