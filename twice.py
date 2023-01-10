def twice(list1):
    dict1={}
    set1=set()
    for item in list1:
        if not item in dict1:
           dict1[item]=1
        else:
            dict1[item]+=1
    for item in dict1:
        if dict1[item]==2:
            set1.add(item)
    return set1
a=[1, 3, 1, 4, 3, 7, -2, 0, 7, -2, -2, 1]
print(twice(a))
            
         