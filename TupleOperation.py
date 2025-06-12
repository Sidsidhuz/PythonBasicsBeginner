tup = ("Sidharth", 25, "AI", "Python", 25, "AI")

# >>> Length of the tuple
print(len(tup))

# >>> Count of a particular element
print(tup.count("AI"))

# >>> Index of a particular element (first occurrence)
print(tup.index("Python"))

# >>> Check if an element exists
print("AI" in tup)
print("ML" in tup)

# >>> Concatenate tuples
tup2 = ("Developer", "India")
new_tup = tup + tup2
print(new_tup)

# >>> Repeat tuple
print(tup * 2)

# >>> Convert tuple to list (for modification)
tup_list = list(tup)
tup_list[1] = 30  # Modify an element
tup = tuple(tup_list)
print(tup)

# >>> Unpack tuple elements into variables
name, age, domain, lang, age2, domain2 = tup
print(name, age, domain)

# >>> Nested Tuple
nested = ("AI", (1, 2, 3))
print(nested[1])
print(nested[1][0])
