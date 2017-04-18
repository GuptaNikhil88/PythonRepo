def is_prime(x):
    flag = True
    if(x <= 1):
        flag = False
    if(x>2):
        for n in range(2,x-1):
            if(x%n == 0):
                flag = False
                break
          
    return flag