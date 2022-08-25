# A set is a collection of unordered, unique and immutable elements.
""" my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove(3) # remove only the first element that matches the value, if there are more than one, it will raise an error.
print(my_set)
my_set.discard(3) # discard removes the element if it is present in the set.
print(my_set)
my_set.update([7, 8, 9]) 
print(my_set)
my_set.pop() # removes and returns an arbitrary element from the set.
print(my_set)
my_set.clear()
print(my_set)

empty_set = set() """

# set operations
# union, intersection, difference, symmetric difference
# union: returns a new set with all the elements from both sets.
# intersection: returns a new set with all the elements that are in both sets.
# difference: returns a new set with all the elements that are in the first set but not in the second set.
# symmetric difference: returns a new set with all the elements that are in one set but not in the other set.

set1 = set(x for x in range(20) if x % 2 == 0 and x % 3 == 0)
set2 = set(x for x in range(20) if x % 5 == 0 or x % 7 == 0)
print(set1)
print(set2)

print(set1.union(set2)) # u = set1 | set2
print(set1.intersection(set2)) # i = set1 & set2
print(set1.difference(set2)) # dif = set1 - set2
print(set2.difference(set1)) #dif = set2 - set1
print(set1.symmetric_difference(set2)) # d = set1 ^ set2
