
# def sum(l):
#   for i in l:
#     add=0
#     add=add+l[i]
#     return add
# print(sum([1,2,3,4,5,6,7,8,9]))


def sum_all(*args):
  sum=0
  for i in args:
    sum+=i
  return sum


print(sum_all(1,2,3,4,5))


