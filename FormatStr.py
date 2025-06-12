#Format String

# >>1 using .format and {}
name = "Sidharth"
place = "Peringome"
age = 23
print("1.The name is {} and place is {}\n".format(name, place))


# >>2  using .format with Index
print("2.The name is {1} and place is {0} \n".format(name, place))

# >>3 using .format with key
print("3.The name is {a} and place is {b}\n".format( a=name,b=place))

# >>4 using Dictionary
abt = {"Name":"sidharth", "place":"peringome"}
print("4.The name is {data[Name]} and place is {data[place]}\n".format(data = abt))

# >> using %
print("5.My name is %s and my age is %d\n" % (name, age))

# >> using f keyword
print(f"6.My name is {name} and my age is {age}\n")
