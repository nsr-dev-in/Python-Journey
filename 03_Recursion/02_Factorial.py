#WAP TO PRINT FACTORIAL SERIES USING RECURSION

def factorial(n):
    #BASE CASE
    if n==1 or n==0:
        return 1

    #RECURSIVE CALLS
    return n * factorial(n-1)

#FUNCTION CALL

print(factorial(5))
