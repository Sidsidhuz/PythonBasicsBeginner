import pandas as pd

# s = pd.Series([10,52,63])
# print(s)
# s1 = pd.array([[1,2,3],[4,5,6]])
# print(s1)
di = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
di1 = pd.Series(di)
# print(di1[1:])
# print(f"{di1} is ")
print(di1.axes)
print(di1.values)
print(di1.index)
print(di1.describe())
print(di1.ndim)
print(di1.empty)
print(di1.size)

# data = {
#     'State': ['Kerala', 'Tamil Nadu', 'Karnataka', 'Maharashtra','Rajasthan'],
#     'Capital': ['Thiruvananthapuram', 'Chennai', 'Bengaluru', 'Mumbai','Jaipur'],
#     'Population_M': [35.7, 77.8, 67.9, 126.4,3.0]
# }
# dframe = pd.DataFrame(data)



