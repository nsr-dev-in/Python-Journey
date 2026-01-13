n=int(input("Enter Number : "))

s_even=n*(n+1)
s_odd=n**2


print(s_odd,s_even)

def gcd(s_odd,s_even):
    if s_even==0:
        return s_odd
    return gcd(s_even,s_odd%s_even)

print(gcd(s_odd,s_even))