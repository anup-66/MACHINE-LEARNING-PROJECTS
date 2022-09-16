# a = int(input())
# arr = input().split()
# Pair = len(arr)//a
# Arr=[]
# Final=[]
# for ii in range(0,len(arr),len(arr)//a):
#     Arr.append(arr[ii])
# Arr.sort()
# A=0
# while A<len(Arr):
#     temp = Arr[A]
#     for el in range(len(arr)):
#         if(arr[el]==temp):
#             for ij in range(el,el+Pair):
#                 Final.append(arr[ij])
#     A+=1
#
# print(Final)
# A = int(input("enter no. of starts : "))
# # A=5
# k = 2*A-4
# for h in range(int(input("enter no. of design : "))):
#
#     for i in range(1, A + 1):
#         if (k == -2):
#             print("*" * i * 2)
#         else:
#             print("*" * i, " " * k, "*" * i)
#         k = k - 2
#     x = 0
#     for p in range(A - 1, 0, -1):
#         if (x == 0):
#             print("*" * i * 2)
#         else:
#             print("*" * p, " " * x, "*" * p)
#         x += 2
#     k=2*A-4
