def switch_pairs(a):
    for i in range(0,len(a)-1,2):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    return a

print([1, 2, 3,4,5,6,7,8])
print(switch_pairs([1, 2, 3,4,5,6,7,8,9]))
   