print(" this is a line 1")

def name(one, two):
    """
    Purpose: one
    """
    
# end def

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# hala inaro zadam to branch fibo



