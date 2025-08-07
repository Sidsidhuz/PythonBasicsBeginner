import pandas as pd


# s = pd.Series([10,52,63])
# print(s)
# s1 = pd.array([[1,2,3],[4,5,6]])
# print(s1)
# di = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
# di1 = pd.Series(di)
# # print(di1[1:])
# # print(f"{di1} is ")
# print(di1.axes)
# print(di1.values)
# print(di1.index)
# print(di1.describe())
# print(di1.ndim)
# print(di1.empty)
# print(di1.size)

# data = {
#     'State': ['Kerala', 'Tamil Nadu', 'Karnataka', 'Maharashtra','Rajasthan'],
#     'Capital': ['Thiruvananthapuram', 'Chennai', 'Bengaluru', 'Mumbai','Jaipur'],
#     'Population_M': [35.7, 77.8, 67.9, 126.4,3.0]
# }
# dframe = pd.DataFrame(data)
#
# s1 = pd.Series([1,2,3,4,5,None], index=['a','b','c','d','e','f'])
# s2 = pd.Series([6,7,8,9,10], index=['a','b','c','d','e'])
# # print(s1+s2)
# # print(s2.apply(lambda x: x*x))
# # # print(s1.head(1))
# # # print(s2.tail(2))
# # # print(s1[s1>3])
# # print(s1.isnull())
# # s1.fillna(0)
# # print(s1)
# # s3 = pd.Series([5,2,4,1,3], index=['a','c','d','b','e'])
# # print(s3.sort_values(ascending=False))
# # print(s3.sort_index(ascending=False))
# s4 = pd.Series([10,20,21,22,23,24,25,30,20,50,37,49,40,50,63,28,11,9,9,48,49])
# # print(s4.between(10,20))
# # print(s4.bfill())
# # print(s4.ffill())
# # print(s4)
# # print(s4.where(s4>20))
# # print(s4.duplicated(keep='first'))
# # print(s4.drop_duplicates())
# print(s4.value_counts())
# print(s4.unique())
#
data = {
    'State': ['Kerala', 'Tamil Nadu', 'Karnataka', 'Maharashtra','Rajasthan'],
    'Capital': ['Thiruvananthapuram', 'Chennai', 'Bengaluru', 'Mumbai','Jaipur'],
    'Population_M': [35.7, 77.8, 67.9, 126.4,3.0],
    'Literacy Rate':[100,69,70,46,35]
}
dframe = pd.DataFrame(data)
# print(dframe)

data2 = [{'a':1,'b':2},{'a':3,'b':4,'c':5}]
dframe2 = pd.DataFrame(data2,index=['r1','r2'])
# print(dframe2)

data3 = [['alex',18],['bob',19],['Alice',18]]
dframe3 = pd.DataFrame(data3,columns=['Name','Age'],index = [1,2,3])
# print(dframe3)
data4 = {'one':pd.Series([1,2,3], index = ['a','b','c']),
         'two':pd.Series([1,2,3,4], index = ['a','b','c','d']),
         'three':pd.Series([1,2,3,4,5],index = ['a','b','c','d','e']),
         'four':pd.Series([1,2,3,4,5,6],index = ['a','b','c','d','e','f'])}
df = pd.DataFrame(data4)
# print(df)
df['five'] = pd.Series([1,2,3,4,5,6,7],index = ['a','b','c','d','e','f','g'])
# df.pop('five')
# print(df)
# print(df[['one','two']])
# print(df[df['four']>3])
df.insert(4,'six',[1,2,3,4,5,6])
print(df)