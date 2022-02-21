def puzzle():
    r=(numlegs)/2-numheads
    c=numheads-r
    return(r, c)
numlegs=94
numheads=35
print(puzzle())
