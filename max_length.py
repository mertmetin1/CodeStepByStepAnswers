def max_length(setofstring):
    list1=[]
    if setofstring=={}:
        return 0
    for item in setofstring:
        list1.append(len(item))
    return max(list1)
        
        
myset = {"apple", "banana", "cherry"}      
print(max_length(myset))
        
    