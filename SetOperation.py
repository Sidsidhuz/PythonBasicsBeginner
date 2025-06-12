set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# >>> Add an element to the set
set1.add(6)
print(set1)

# >>> Add multiple elements (update)
set1.update([7, 8])
print(set1)

# >>> Remove element (raises error if not found)
set1.remove(8)
print(set1)

# >>> Discard element (no error if not found)
set1.discard(10)
print(set1)

# >>> Pop random element (sets are unordered)
print(set1.pop())

# >>> Clear all elements
set3 = {9, 10}
set3.clear()
print(set3)

# >>> Delete set completely
# del set3

# >>> Union (all elements)
print(set1.union(set2))  # or set1 | set2

# >>> Intersection (common elements)
print(set1.intersection(set2))  # or set1 & set2

# >>> Difference (elements in set1 but not in set2)
print(set1.difference(set2))  # or set1 - set2

# >>> Symmetric Difference (elements not common)
print(set1.symmetric_difference(set2))  # or set1 ^ set2

# >>> Check if set1 is subset of set2
print(set1.issubset(set2))

# >>> Check if set1 is superset of set2
print(set1.issuperset(set2))

# >>> Check if sets are disjoint (no common elements)
print(set1.isdisjoint(set2))
