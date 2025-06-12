val = "my name is Sidharth"

# >>> Convert elements into uppercase
print(val.upper())

# >>> convert elements into lowercase
print(val.lower())

# >>> convert the first element in a string to uppercase
print(val.capitalize())

# >>> Convert 1st letter of each word into uppercase
print(val.title())

# >>> Convert lower to upper and upper to lower
print(val.swapcase())

# >>> returns the index of the specified element in a string  #Note : returns error if element not found
print(val.index("S"))
print(val.index("m",0,8))

# >>> returns count of the specified element
print(val.count("S"))

# >>> returns the index of the specified element. # Note : return -1 if element not found
print(val.find("S"))


# >>>
print(val.replace("S","m", 1))

# >>> check whether the str starts or ends with the specified
print(val.startswith("m"))
print(val.endswith("h"))

# >>> remove spaces from left and right side of a string or removes the specified character
val = "  sid   "
print(val.strip())
print(val.lstrip())
print(val.rstrip())
val = ">>sid<<"
print(val.strip("<>")) # removes  > and  < from the both ends of the string
