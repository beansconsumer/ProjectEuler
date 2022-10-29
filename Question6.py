
def sum_of_squares(n):
    a = 0
    for i in range(1,n+1):
        b = i**2
        a = a + b
    return a

def square_of_sum(n):
    a = 0
    for i in range(1,n+1):
        a = a + i
    return a ** 2
    

def difference(n):
    a = sum_of_squares(n)
    b = square_of_sum(n)
    dif = b - a
    print(dif)
    
difference(100)
