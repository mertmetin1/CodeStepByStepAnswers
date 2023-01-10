def coin_flip(inputfile):
    dosya=open(inputfile)
    kelimeler= dosya.read().split()
    hcount=0
    tcount=0
    
    for item in kelimeler:
        if item[0]=="H":
            hcount+=1
        if item[0]=="h":
            hcount+=1
        if item[0]=="T":
            tcount+=1
        if item[0]=="t":
            tcount+=1
    percent=hcount/(tcount+hcount)*100
    print()
    if percent>=50:
        print(hcount,"heads ("+str(percent)+"%)")
        print("You win!")  
    else:
        print(hcount,"heads ("+str(percent)+"%)")
        print("You lose!")    
    
            
 

    
    
    
    
coin_flip("C:\\Users\\90506\Desktop\\vs code\\2.sınıf1.dönem\\homework2\\headortail.txt")