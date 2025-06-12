#swap keys with value
d = {1:'hi',2:'hello'}
val = []
key = []
for i in d:
    val.append(d[i])
    key.append(i)
newDict = dict(zip(val,key))
print(newDict)