d, c = map(int, input().split())
cntr=0
if d<500:
    for i in range(2, d):
        if d%i==0:
            cntr=cntr+1
    if c%2==0 and cntr==0:
        print('Good job!')
    else:
        print('Try next time!')
else:
    print('Try next time!')
