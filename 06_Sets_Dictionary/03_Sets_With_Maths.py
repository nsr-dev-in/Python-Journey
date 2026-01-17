set1={2,4,6,8,10}
set2={1,2,4,6,7,9,10}

# UNION
print(set1|set2)

# INTERSECTION
print(set1&set2)

# DIFFERENCE
print(set1-set2)
print(set1.difference(set2))

print(set2-set1)
print(set2.difference(set1))

# SYMMETRIC DIFFERENCE -- NON COMMAN ELEMENTS
print(set2^set1)
print(set2.symmetric_difference(set1))


