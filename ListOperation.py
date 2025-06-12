from itertools import count

l = [1,2.3,True,"Sid",[1,2,3],{4,5,6},{1:2,3:5}]
l1 = ['sid','dharth']
l2 = [1,2,3,4,5,6,7,'a']


l.extend(l1)
print(l)

# del method
del l1[0]

# .remove() Removes the specified element from the list
l.remove('dharth')

# .pop() Removes the element from the specified index postion
l.pop(-1)

# .clear() is used to delete the entire elements in the list
l2.clear()

l3 =[True,False,True,True,False]

# reverse the order of the list
l3.reverse()
print(l3)
print(min(l3))
print(max(l3))
print(l3.count(True))


