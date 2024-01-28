# num=1
# while num<5:
#     print("Num=",num)
#     num+=1
# else:
#     print("While ended")
# import time
# num=1
# while True:
#     print(num)
#     num+=1
#     time.sleep(0.1)
#     if num==20:
#         break
# else:
#     print("count ended")
# import random
# floor=1
# energy=random.randint(30,60)
# print(f"i am on the {floor} floor ")
# while floor!=5:
#     step=0
#     while step!=20:
#         step+=1
#         energy-=1
#         if energy==0:
#             print("I am tired! I will rest!")
#             print("I will take an elevator!")
#             energy +=30
#             break
#     floor+=1
#     print("Now I am on the ",floor,"floor")
# print("I am on the right floor")
# i=0
# start=1
# end=100
# while start<end:
#     start+=1
#     i+=1
# print("count item",i)
# sum=0
# i=0
# count=0
# while i<20:
#     i+=1
#     sum+=i
#     count+=1
# print("sum=",sum/count)
# while i<30:
#     if i%2==0:
#         print(i)
#     i+=1
# rand_num=random.randint(1,10)
# user_num=0
# tries=5
# while rand_num!=user_num:
#     user_num=int(input("Enter num 1-10:"))
#     tries-=1
#     if tries==0:
#         print("Game over!")
#         break
#     else:
#         if user_num<rand_num:
#             print("try bigger!")
#         else:
#             print("try lower!")
# else:
#     print("Win!")
#for elem in itereible
# for i in range(10,20,2):
#     print(i)
# for s in "hello":
#     print(s,end=" - ")
# print("\nqwerty")
# for num in range(100):
#     print(num)
#     if num==5:
#         break
number=int(input("Enter number:"))
for i in range(number):
    print(i)
first=int(input("Enter:"))
second=int(input("Enter:"))
if first>second:
    first,second=second,first
print(f"Enter from {first} to {second}:")
for i in range(first,second):
    print(i)
for i in range(first,second):
    if number%2==0:
        print("Even=",i)
for i in range(first,second):
    if number%2!=0:
        print("Odd=",i)
for i in range(first,second):
    if number%7==0:
        print("//7=",i)
first=int(input("Enter:"))
second=int(input("Enter:"))
sum=0
for i in range(first,second):
    sum+=i
print("Sum=",sum)
sum=0
while True:
    number=int(input("Enter number:"))
    if number==0:
        break
    sum+=number
print("sum=",sum)
k=int(input("Enter number of option:"))
for i in range(2,11):
    multiplication=k*i
print(f"{k}*{i}={multiplication}")
while True:
    print("1-hryvnia\n2-dollar\n3-euro")
    choose=int(input("Enter number of currency:"))
    sum=int(input("Enter sum which you want to convert:"))
    if choose==1:
        rate=3.3
    elif choose==2:
        rate=1
    else:
        rate=2.6
    print(f"The amount is:{sum*rate}")
first=int(input("Enter:"))
second=int(input("Enter:"))
while True:
    number=int(input("Enter number:"))
    if first<=number<=second:
        print(f"{number}is in the range")
    else:
        print("Try again")







