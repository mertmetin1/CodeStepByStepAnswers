def flip_half(inputlist):
    if len(inputlist)%2==1:
        for item in range(len(inputlist)//2+1):
            if item%2==1:
                temp= inputlist[item]
                inputlist[item]=inputlist[len(inputlist)-item-1]
                inputlist[len(inputlist)-item-1]=temp
    else:
         for item in range(len(inputlist)//2+1):
                if item%2==1:
                    temp= inputlist[item]
                    inputlist[item]=inputlist[len(inputlist)-item]
                    inputlist[len(inputlist)-item]=temp     
           
    return inputlist
           
            
        





