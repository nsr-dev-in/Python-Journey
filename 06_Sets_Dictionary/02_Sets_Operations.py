my_set={1,2,3,4,5}
print(my_set)

my_set.add(12)
print(my_set)

my_set.discard(5) # gives no error else
print(my_set)

my_set.remove(4) # gives error if element not present there
print(my_set)

my_set.add("Hello")
print(my_set)

if "Hello" in my_set:
    print("present")
else:
    print("Not Present")

my_set.clear()
print(my_set)

#my_set me indexing nhi hoti

set1={1,2,3}
set2=set1

set2.add(4)
print(set1)
print(set2)

set3=set2.copy() #sallow copy without address

