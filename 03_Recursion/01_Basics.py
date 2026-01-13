# PRINT 1 TO N USING RECURSION

# WHILE LOOP
i=1
n=int(input("Enter Number : "))
while i<=n:
    print(i,end=" ")
    i+=1
print(" ")

# RECURSION FUNCTIONS
def printnnumbers(i,n):
    #BASE CASE -- STOPPING CONDITION
    if i>n:
        return
    
    #RECURSIVE CASE -- KAISE CHLYGA
    print(i,end=" ")
    printnnumbers(i+1,n)

#FUNCTION CALL
printnnumbers(1,5)
