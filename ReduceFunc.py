from functools import reduce as rd

# nums = [1, 2, 3]
#
# result = rd(lambda x, y: x + y, nums,10)
# print(result)

#
# num = [3,7,1,8,2,9]
# def find_min(a,b):
#     return a if a < b else b
# print(rd(find_min,num)) # during the first iteration a,b are taken from the list from there on the result of the previous output is served as first input
#
string = "a citizen of ekm fought and won the election"
stop_words = ['in', 'of', 'a', 'and', 'the']

# def rem_stp(s):
#     stop_words = ['in', 'of', 'a', 'and', 'the']
#     L = s.split()
#     nl = ''
#     for i in L:
#         if i.lower() not in stop_words:
#
#             nl += ' ' + i
#     print(nl)
# rem_stp(string)


# def stp(a):
#     return a not in stop_words
# print(" ".join(filter(lambda x: x not in stop_words, string.split())))

num = [1.2,2.3,3.4]
print(list(map(lambda x :int(x),num)))
