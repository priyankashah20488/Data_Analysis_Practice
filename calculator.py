def add(x,y,*num):
    '''Returns addition of x and y and also with n number '''
    s = x+y
    for i in num:
        s+=i
    return s    