while True:
    add1=float(input('enter your number? '))
    add2=float(input('enter your number? '))
    if add1==0 and add2==0:
        break
    if add1>add2:
        print('add1 is bigger')
    else:
        print('add2 is bigger')
