def int_to_digits(n):
    '''
    Returns a list of digits of an integer.
    '''
    digits = []

    def digits_inner(i):
        if i == 0:
            return digits
        digits.append(i%10)
        digits_inner(i//10)
    
    
    if n > 0:
        digits_inner(n)
    elif n == 0:
        digits = [0] # two zeros needed here
    else:
        # Handle negative integers
        digits_inner(-n)
        digits = [-d for d in digits]
    digits.reverse()
    return digits

ds = int_to_digits(-345)
print(ds)
