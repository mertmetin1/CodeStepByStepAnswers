def plus_scores(text):
    f=open(text,"r")
    icerik=f.readlines()
    print(icerik)
    
    for item in range(0,len(icerik),2):
        count=0
        print(icerik[item])
        for k in range(len(icerik[item+1])):
            if icerik[item+1][k]=="+":
                count+=1
        print(icerik[item+1])
        print(count*100/len(icerik[item+1]))
                
            
            
        
           
        
            
        
    
    
    
    
    
plus_scores("C:\\Users\\90506\\Desktop\\vs code\\2.sınıf1.dönem\\homework2\\names.txt")