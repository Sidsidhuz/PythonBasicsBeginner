import numpy as np
#[1,2,3,4]
#[[1,2,3,4],[1,2,3,4]]
#[[[1,2,3,4],[1,2,3,4]]]
# val=np.array([1,2,3,4])
# print(val)
# print(type(val))
# print(val.ndim)
# print(val.shape)
#
# val=np.array([[1,2,3,4],[10,20,30,40]])
# print(val)
# print(val.ndim)
# print(val.shape)
#
# val=np.array([[[1,2,3,4],[10,20,30,40]],[[1,2,3,4],[10,20,30,40]]])
# print(val)
# print(val.ndim)
# print(val.shape)
# print(val.itemsize)
# print(val.nbytes)
# print(val.size)
#
# val=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[80,90,100,110,120,130,140]])
# print(val)
# print()
# print(val[1])
# print(val[1,5])
# print(val[1:])
# print(val[1:,1:3])
# print(val[0,2:])
# print(val[1:,1:5:2])
#
# val=np.array([[1,2,3,4],[10,20,30,40]])
# print(val)
# val[1,3]=400
# print(val)
# val[0:,1]=[20,200]
# print(val)
#
# val=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(val)
# print()
# print(val[1])
# print(val[1,1])
# print(val[1,1,0])
# val[0,0:]=[[100,200],[300,400]]
# print(val)
# val[0,:]=10
# print(val)
# print(np.random.randint(1,10,size=(3,2,2)))
# arr = np.array([[1,2,3,4,5]])
# print(np.repeat(arr,5,0))
# print(np.zeros(5))
# print(np.zeros((2,5)))
# print()
# print(np.ones((2,5)))
# print(np.identity(3))
# # arr = [[[5,2],[5,7]],[[2,7],[1,5]],[[7,9],[8,3]]]
# arr1 = np.array([[[5,2],[5,7]],[[2,7],[1,5]],[[7,9],[8,3]]])
# new = np.copy(arr1)
# new[[0]] = 100
# print(new)
# print(new.shape)
# arr = np.array([1,2,3,4])
# print(arr + 2)
# print(arr - 2)
# print(arr * 2)
# print(arr ** 2)
# print()
# arr1 = np.array([1,2,3,4])
# print()
# print(arr1 + arr)
# print(arr1 - arr)
# print()
# print(np.tan(arr1))
#
# arr2 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
# # for i in arr2:
# #     print(i)
# #     for j in i:
# #         print(j)
# #         for k in j:
# #             print(k)
# res = np.nditer(arr2)
# for i in np.nditer(arr2,op_flags = ['readwrite']):
#     i[...] = i * 10
#     print(i)
# # print(arr2.flat)
# # for i in arr2.flat:
#     print(i)
# def sqr(x):
#     return x*x
# def add(a,b,c):
#     return a+b+c
#
# arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print(sqr(arr))
# sqrd = np.vectorize(sqr)
# added = np.vectorize(add)
# print(added(arr1,arr2,arr3))
# # print(sqrd(arr))
# print(np.ones((3,4)))
# print(np.full((5,5,5), 4))
# a = np.array([[1,2,3,2,5,6],[2,7,8,5,9,3],[4,5,6,8,9,2],[8,1,0,3,7,4],[9,8,7,6,4,5],[1,2,3,4,5,6]])
# # print(np.linalg.det(a))
# # print(np.linalg.inv(a))
# print(np.min(a))
# print(np.max(a))
# print(np.mean(a))
# print(np.std(a))
# print(np.median(a))
# before = np.array([[1,2,3],[4,5,6]])
# after = before.reshape(3,2)
# # print(before)
# print(after)
# print(np.matmul(before,after))
a = np.array([1,2,3,4,5])
b= np.array([6,7,8,9,10])
# print(np.vstack((a,a,a,b)))
# print(np.hstack((a,a,a,b)))

print(np.arange(5))
print(np.arange(5,9))
print(np.arange(5,9,2))
print(np.arange(1,9,2).reshape(2,2))

print(np.linspace(0,1,10))
print(np.linspace(0,1,10).astype(int))

before = np.array([[1,2,3],[4,5,6]])
print(before.ravel())


