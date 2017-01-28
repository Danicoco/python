def power(a, b):
    if( type(a) == int or type(a)== float)  and (type(b) ==int  or  type(b)== float):

        if b == 0:
            return 1
        else:
            return a * power(a, b-1)
    else:
        raise TypeError("Argument must be integer or float")

print power(2, 4)

