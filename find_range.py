def find_range(inputlist):
    min1=min(inputlist)
    max1=max(inputlist)
    return max1-min1+1


liste=[8, 3, 5, 7, 2, 4]

print(find_range(liste))