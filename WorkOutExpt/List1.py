# remove duplicate values from a list without set
l = [24,36,43,54,1,1,2,3,5,9,24]
k = []
for i in l:
    if i not in k:
        k.append(i)
print(k)



