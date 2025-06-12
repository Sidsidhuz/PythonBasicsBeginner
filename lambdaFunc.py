a = lambda x,y:x*y
print(a(3,2))
#####################################################
great = lambda x,y:'hai' if x>y else 'hello'
print(great(3,2))

#############################################
# l = ['ab','abc','a','aaa',3,2,5,9,8]
# l.sort()
#
# print(l)
############################################3
def fun(v = 2):
    c = v ** 2
    return c
x = 2
high = lambda x,i:x+i
print(high(3,fun()))