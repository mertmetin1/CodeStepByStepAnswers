def num_in_common(list1,list2):
    list3=[]
    for item in list1:
       if item in list1:
           if item in list2:
            list3.append(item)
    finallist=set(list3)
    return len(list(finallist))
l1=[3, 7, 3, -1, 2, 3, 7, 2, 15, 15]
l2=[-5, 15, 2, -1, 7, 15, 36]
print(num_in_common(l1,l2))
      
            