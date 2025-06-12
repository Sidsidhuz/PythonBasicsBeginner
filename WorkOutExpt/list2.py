# count frequency of elements in a list
l = [1,2,3,4,1,2,3,1,2,1]
k = []
dic = dict()
for i in l:
    if i not in k:
        k.append(i)

for i in k:
    dic.update({i:l.count(i)})

# print(dic)
for i in dic:
    print(f"{i} : {dic[i]}")



