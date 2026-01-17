# DICTIONARY KE OPERATIONS SIRF KEYS PAR HOTI HAIN

dict2={1:"A",2:"B",3:"C",4:"D",}

print(dict2[1]) # dict2[key]--> O/P Value of that key
print(dict2[2]) # dict2[key]--> O/P Value of that key
print(dict2[3]) # dict2[key]--> O/P Value of that key
print(dict2[4]) # dict2[key]--> O/P Value of that key

# print(dict2['A']) # ERROR

Btech={1:"Abhi",2:"Bairav",3:"Chintan",4:"Dhruv",}
print(Btech)

#ADD 2 MORE STDS
Btech[5]="Pratham"
print(Btech)

Btech[3]="Pathan" #REPLACE INSTEAD OF ADDING
print(Btech)

#REMOVE 
Btech.pop(2)
print(Btech)

del  Btech[1]
print(Btech)

