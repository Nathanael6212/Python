# recursion
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(9))



def fibonacci(n):
    a=0
    b=1
    if n<0:
        print("incorrect number")
    elif n==0 or n==1:
        return n
    else:
        for i in range (1,n):
            c=a+b
            a=b
            b=c
        return b
print(fibonacci(0))