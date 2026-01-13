def func(n):
    if n==0:
        return
    
    #function call krdiya maine output liye toh stack me load ho jyga ans 
    func(n-1)
    print(n,end=" ")

func(5)