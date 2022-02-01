a=int(input())
for i in range(0, a):
    x=int(input())
    if x<=10:
        print('Go to work!')
    if x>10 and x<=25:
        print('You are weak')
    if x>25 and x<=45:
        print('Okay, fine')
    if x>45:
        print('Burn! Burn! Burn Young!')