#fibanocci
i = int(input("Enter a number: "))
sum = [0,1]
for i in range(2,i):
    sum.append(sum[-1]+sum[-2])
print(sum)




