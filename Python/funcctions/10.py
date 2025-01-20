# def factorial(n):
#   fact=1
#   while n>1:
#     fact*=n
#     n=n-1
#   return fact
# print(factorial(5)) 


def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1)
print(factorial(5))
