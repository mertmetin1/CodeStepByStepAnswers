def index_of(inputlist,sayı):
    a=-1
    for item in range(len(inputlist)):
        if sayı==inputlist[item]:
            a=item
            break       
    return a
    

print(index_of([42, 7, -9, 14, 8, 39, 42, 8, 19, 0],8))