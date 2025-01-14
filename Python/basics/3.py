# list =[1,-2,3,-4,5,6,-7,-8,9,10]
# counter=0
# for i in list:
#   if i>0:
#     counter+=1
# print(counter)

# n=int(input("enter the number:"))
# sum =0
# for i in range(n):
#   if i%2==0:
#     sum+=i
# print(sum)

# n=int(input("enter the number:"))
# for i in range(1,n+1):
#   if i==5:
#     continue
#   else:
#     print(n*i)

# name=input("enter name:")
# length=len(name)
# for i in range(length-1,-1,-1):
#   print(name[i],end="")

# char = input("enter a string:")
# count =0
# for i in range(0,len(char)-1):
#   for j in range(1,len(char)-1):
#     if char[i]==char[j]:
#       break
#     else:
#       print(char[i])
#       count+=1
#       break
#   if count==1:
#     break

# str = input("enter a string:")
# for i in str:
#   if str.count(i)==1:
#     print(i)
#     break
  
# n = int(input("enter the number:"))
# factorial=1
# while n>1:
#   factorial*=n
#   n=n-1
  
# print(factorial)


# while True:
#   n= int(input("enter a number between 1 and 10:"))
#   if 1<=n<=10:
#     print("good job")
#     break
#   else:
#     print("try again!")

# n=int(input("enter a number:"))
# for i in range(2,int(n**0.5)+1):
#   if n%i==0:
#     print("NOT PRIME")
#     break
# else:
#     print("PRIME")


# l = ["orange","apple","guava","papaya"]
# flag = True
# for i in range(0,len(l)-1):
#   if l[i] in l[i+1:]:
#     flag=False
# print(flag)

import time
retries =5
attempts =0
wait_time=1
while attempts <retries :
  print("wait_time", wait_time , "attempts",attempts+1)
  time.sleep(wait_time)
  wait_time*=2
  attempts+=1
  

