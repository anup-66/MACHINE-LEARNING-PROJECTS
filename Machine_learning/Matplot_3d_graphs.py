# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
# # fig = plt.figure()
# ax = plt.axes(projection='3d')
# Zline = np.linspace(0,15,1000)
# xline = np.sin(Zline)
# yline = np.cos(Zline)
# ax.plot3D(xline,yline,Zline,'grey')
# zdata = 15*np.random.random(100)
# xdata = np.sin(zdata) #+ .1*np.random.randn(100)
# ydata = np.cos(zdata) #+ .1*np.random.randn(100)
# ax.scatter3D(xdata,ydata,zdata,'Green')
# plt.show()

# cook your dish here
for ii in range(int(input())):
    X = int(input())
    arr = list(map(int,input().split()))
    # print(arr[0])
    count=0
    # print(arr[0]," ",arr[X-1]==X)
    if(arr[0]==1 and arr[X-1]==X):
        print(0)
    else:
        ij=0
        while(ij!=X):
            if ij !=X-1:
                 temp=arr[ij]
                 arr[ij]=arr[ij+1]
                 arr[ij+1]=temp
                 count+=1
                 ij+=1
                 print(arr)
                 if(arr[0]==1 and arr[X-1]==X):
                    print(count)
                    break
            else:
                ij=0