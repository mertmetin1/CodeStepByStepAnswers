def starters(stringlist,count):
    dict1={}
    set1=set()
    for item in stringlist:
        item=item.lower()
        if not item=='':
            if item[0] in dict1:
                dict1[item[0]]+=1
            else:
                dict1[item[0]]=1                
    for item in dict1:
        if dict1[item]>=count:
            #list1.append(item)
            set1.add(item)
            
        
    print(set1)        
    #print(list1)        
   # print(dict1)
    
a={'hi', 'how', 'are', 'He', '', 'Marty!', 'this', 'morning?', 'fine.', '?foo!', '', 'HOW', 'A'}
print(starters(a,2))            
            
        
    