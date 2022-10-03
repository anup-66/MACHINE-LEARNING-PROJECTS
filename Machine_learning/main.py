# # # # # # # cook your dish here
# # # # # # t = int(input())
# # # # # # for tt in range(t):
# # # # # #     hh = int(input())
# # # # # #     arr = input()
# # # # # #     Count=0
# # # # # #     bool=True
# # # # # #     if len(arr)==0:
# # # # # #         print(0)
# # # # # #     elif len(arr)!=0:
# # # # # #         count=0
# # # # # #         for kk in arr:
# # # # # #             count+=1
# # # # # #             if(count<=(hh/2) and kk==")"):
# # # # # #                 Count+=1
# # # # # #                 bool = False
# # # # # #             elif count>hh/2:
# # # # # #                 if (kk=="("):
# # # # # #                     Count+=1
# # # # # #                 if Count==1 and kk==")" and bool:
# # # # # #                     Count+=1
# # # # # #         print(Count)
# # # # # #
# # # # #
# # # # # t = int(input())
# # # # # for tt in range(t):
# # # # #     h = int(input())
# # # # #     s = input()
# # # # #     dense=0
# # # # #     count=0
# # # # #     j=h
# # # # #     if h==1:
# # # # #         print(1)
# # # # #     else:
# # # # #         while(count<h/2):
# # # # #             print(s[count],s[h-count-1])
# # # # #             if s[count]=='(' and s[j-1]==')':
# # # # #                 print(s[count], count)
# # # # #                 dense+=2
# # # # #                 count+=1
# # # # #                 j-=1
# # # # #             elif(s[count]==')' and s[j-1]==')'):
# # # # #                 count+=1
# # # # #             else:
# # # # #                 count+=1
# # # # #                 j-=1
# # # # #                 print(count)
# # # # #         print(h-dense)
# # # # #
# # # # # t = int(input())
# # # # # for tt in range(t):
# # # # #     h = int(input())
# # # # #     s = input()
# # # # #     dense = 0
# # # # #     count = 0
# # # # #     j = h
# # # # #     if h == 1:
# # # # #         print(1)
# # # # #     elif h == 0:
# # # # #         print(0)
# # # # #     else:
# # # # #         while (count < h / 2):
# # # # #
# # # # #             if s[count] == '(' and s[j - 1] == ')':
# # # # #
# # # # #                 dense += 2
# # # # #                 count += 1
# # # # #                 j -= 1
# # # # #             elif (s[count] == '(' and s[j - 1] == '('):
# # # # #                 j -= 1
# # # # #             elif s[count] == ')' and s[j - 1] == ')':
# # # # #                 count += 1
# # # # #             else:
# # # # #                 count += 1
# # # # #                 j -= 1
# # # # #
# # # # #         print(h - dense)
# # # # #
# # # # #         count = 0
# # # # #         if Y >= X:
# # # # #             while ((abs(Y) - abs(X)) != 0):
# # # # #                 Y += 1
# # # # #                 X += 2
# # # # #                 count += 1
# # # # #         elif Y < X:
# # # # #             while ((abs(Y) - abs(X)) != 0):
# # # # #                 Y -= 1
# # # # #                 X -= 2
# # # # #                 count += 1
# # # # #         print(count)
# # # #
# # # # num = int(input())
# # # # if 4 != 0:
# # # #     print(num - 1)
# # # # else:
# # # #     print(num + 1)
# # #
# # # for ii in range(int(input())):
# # #     N = int(input())
# # #     S = input()
# # #     s = ""
# # #
# # #     if (S == S[::-1]):
# # #         print(S)
# # #     else:
# # #         for i in range(len(S)):
# # #             M = S[:i] + S[i + 1:]
# # #             if (M == M[::-1]):
# # #                 s = M
# # #                 break
# # #             for j in range(len(S) - 1):
# # #                 K = M[:j] + M[j + 1:]
# # #                 count+=1
# # #                 # print(K,K[::-1])
# # #                 if K == K[::-1]:
# # #                     s = K
# # #
# # #                     break
# # #
# # #         print(s)
# # #
# # # arr1 = list(map(int,input().split()))
# # # arr2 = list(map(int,input().split()))
# # # count=0
# # # sum=0
# # # sum2=0
# # # for ii in range(len(arr1)):
# # #     for j in range(ii+1):
# # #         sum+=arr1[j]
# # #     # print(sum)
# # #     for k in range(ii+1,len(arr1)):
# # #         sum2+=arr1[k]
# # #     # print(sum2)
# # #     if(sum==sum2):
# # #         count=ii
# # #         break
# # #     sum=0
# # #     sum2=0
# # # print(sum,sum2)
# # # sump=0
# # # for ii in range(count+1):
# # #     sump+=arr2[ii]
# # # sump2=0
# # # for ii in range(count+1,len(arr2)):
# # #     sump2+=arr2[ii]
# # # if sum==sum2 and sump==sump2 and sum==sump:
# # #     print(count+1)
# # # else:
# # #     print(0)
# #
# # # 4,-1,0,3
# # # [1,0,1,2,1,1,7,5]
# # # [0,1,0,1,0,1,0,1]
# #
# # # ar1 = list(map(int, input().split()))
# # # ar2 = list(map(int, input().split()))
# # # win = int(input())
# # # val = 0
# # # val2 = 0
# # # Sum=0
# # # for ii in range(len(ar1)-win):
# # #     temp = 0
# # #     ind=True
# # #     for jj in range(ii+1, ii+win+1):
# # #         if ar2[ii] == 0:
# # #             temp += ar1[jj]
# # #     if temp > Sum:
# # #         Sum = temp
# # #     else:
# # #         ind = False
# # #     if ar2[ii] == 0 and ind:
# # #         val += ar1[ii]
# # # final = val+Sum
# # # print(val)
# # # print(Sum)
# # # print(final)
# # # val = 5 + 2
# # # sum = 2+5+6)  +
# # # 1 5 2 5 6 0 1 0
# # # 1 0 0 1 1 1 1 1
# #
# #
# # # arr = [1,2,3]+[2,4,5]
# # # print(arr)
# #
# #
# #
# #
# #
# # #
# # # def Check(p,q):
# # #     A = p
# # #     B = q
# # #     if(A<B):
# # #         while(A<B):
# # #             A = A*2
# # #             if(A==B):
# # #                 return True
# # #     else:
# # #         while(A>B):
# # #             B = B*2
# # #             if(A==B):
# # #                 return True
# # #     return False
# # #
# # #
# # # print(Check(5,20))
# # #
# # # print(1%2 , "jjjjjjjjj")
# #
# #
# # # for i in range(1,12//2 + 1):
# # #     print(i)
# # # cook your dish here
# # # for ii in range(int(input())):
# # #     N,X,Y = map(int,input().split())
# # #     List = list(map(int,input().split()))
# # #     small = min(List)
# # #     if(len(List)==1 and Y%2!=0):
# # #         print(small^X)
# # #     elif(len(List)==1 and Y%2!=0):
# # #         print(List[0])
# # #     else:
# # #         # for jj in range(len(List) + len(List)):
# # #         for jj in range(Y):
# # #             for ii in range(len(List)):
# # #                 Temp = small ^ X
# # #
# # #                 if (List[ii] == small):
# # #                     List[ii] = Temp
# # #                     small = min(List)
# # #         List.sort()
# # #         print(*List)
# #
# #
# # k=18
# # flag=False
# # A = [1,2,3,6,5,6,7,8,9]
# # for i in A:
# #     y=k-i
# #     for j in range(y):
# #         if(y==A[j]):
# #             flag=True
# #             print(i ," " ,A[j])
# #             break
# #     if(flag):
# #         break
# #
# # if(flag):
# #     print("Yes")
# # else:
# #     print("NO")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import tensorflow as tf
# import os
# # from tensorflow.keras import datasets,layers,models
# # from sklearn.model_selection import train_test_split
# from matplotlib.pyplot import annotate
# from tensorflow.keras.utils import load_img,img_to_array
# # from tensorflow.keras import datasets,layers,models
# # import matplotlib.pyplot as plt
#
# # (train_image,train_label),(test_imaage,test_labels) = datasets.cifar10.load_data()
# PATH = os.getcwd()
# from IPython.display import display,Image
#
# Galaxy_path = PATH + "\CutoutFiles\galaxy"
# Galaxy_batch = os.listdir(Galaxy_path)
# x_train = []
# Galaxy_path +="\\"
# count=0
# class_names = ['galaxy','star']
# # plt.figure(figsize=(10,10))
#
# # # if data are in form of images
# for sample in Galaxy_batch:
#     img_path = Galaxy_path + sample
#     x = load_img(img_path)
#     # x = x/255
#     x = img_to_array(x)
#     # reshape into a single sample with 3 channels
#     # x = x.reshape(1, 224, 224, 3)
#     # center pixel data
#     x = x.astype('float32')
#     x = x - [123.68, 116.779, 103.939]
#     # preprocessing if required
#     x_train.append(x)
#
# annotations = annotate([x_train],xy=(0.5, 0.5),option=['galaxy'],display_fn=lambda filename: display(Image(filename)))
# # train_image,test_image = train_image/255.0,test_imaage/255.0
#
#
# # class_names = [['galaxy'],['star']]
# # # plt.figure(figsize=(10,10))
# # plt.figure(figsize=(10,10))
# # for i in range(25):
# #     plt.subplot(5,5,i+1)
# #     plt.xticks([])
# #     plt.yticks([])
# #     plt.grid(False)
# #     plt.imshow(x_train[i], cmap=plt.cm.binary)
# #     # The CIFAR labels happen to be arrays,
# #     # which is why you need the extra index
# #     plt.xlabel(class_names[1])
# # plt.show()

for ii in range(int(input())):
    n = int(input())
    SSEt = {}
    val=True
    for j in range(n):
        SSEt.add()

























