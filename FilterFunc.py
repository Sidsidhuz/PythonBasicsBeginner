# FILTER FUNCTION
from functools import reduce

#filter (Function, Sequence)

# h = filter(lambda x: x % 2 == 0,range(1,11))
# print (list(h))
#
# #
# def vowel(word):
#     return word in 'aeiou' or word in 'AEIOU'
# val = "Sidharth TV"
# print("-".join(filter(vowel,val)))

data = [0,1,'',None,'python',8,'sidharth']
print(list(filter(None,data))) # prints element avoiding all the none element such as False , empty str, 0

# l = [2,3,3,7,4,12,1,16,22,23,27]
#
# def great(x):
#     if x > 10 and x % 2 == 0:
#         return x
# print(list(filter(great,l)))
# print(list(filter(lambda x:x%2==0 and x >10,l)))

