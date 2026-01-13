#WAP FOR FINDING THE GCD OF THE 2 NUMBERS 

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(gcd(10,35))