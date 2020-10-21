def fact(n):
    if n<0:
        print("Sorry factorial does not exist for negative numbers")
    else:
        fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact
n = int(input("Enter the number:"))
print("factorial of",n, "is ",fact(n))
