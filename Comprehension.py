# # comprehension
# import math,pyttsx3
# l = [i**2 for i in range(10)]
# print( [int(math.sqrt(i)) for i in l] )
# eve = [i for i in l if i %2 == 0]
# print(eve)
#
# def speak(text,lang='en'):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
# l = ['devin','dainty','david']
# m = ['abin','ram','luke','jabbar']
# k = [f"{i} {j}" for i in l for j in m]
#
# print(k)
# # speak(k)
# # for i in l:
# #     for j in m:
# #         print(i,'',j, end =' , ')
#
# # l = [1,2,3,4,5]
# # m = [i**2 for i in l]
# # d =  dict(zip(l,m))
# # print(d)

key = ['devin','dainty','david']
value = ['python','cyber','analyst']
print({i:j for i,j in zip(key,value)})
ls = [1,2,3,4,5,6]
res = tuple(i for i in ls if i % 2 == 0)
print(res)

p = zip(key,value)

print(next(p))
print(next(p))

print(iter(key))

