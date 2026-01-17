list1=["ram","gyan","rj","pk","meena","rohit","nsr","meena","rj","pk","nsr","meena","rj","pk"]

freq={} #EMPTY DICTIONARY

#iterate the list wrt unique elements
for name in list1:
    if name not in freq:
        freq[name]=1

    #increase count
    else:
        freq[name]+=1
    
print(freq)

