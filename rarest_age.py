def rarest_age(dict1):
    dict2={}
    if dict1=={}:
        return 0   
    for item in dict1.values():
        if item in dict2:
            dict2[item]+=1
        else:
            dict2[item]=1
    a=min(dict2.values())   
    print(dict2)
    value = {i for i in dict2 if dict2[i]==a}
    return min(value)
    
             
    
   
    
    
a={'A': 1000, 'C': 101, 'D': 3, 'J': 1000, 'K': 101, 'L': 3, 'M': 1000, 'N': 101, 'R': 3, 'S': 1000, 'T': 101, 'V': 3, 'W': 1, 'X': 1, 'LN': 1, 'B': 1, 'Y': 1, 'Z': 1}
print(rarest_age(a))