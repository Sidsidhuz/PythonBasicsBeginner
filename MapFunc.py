# MAP FUNCTION
# map(function,sequence) --> Syntax
# l = lambda x : x*2
# l1 = ['a','b','c','d']
# h = list(map(l,l1))
# print(h)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print(list(map(lambda x,y,z:x+y+z,a,b,c)))