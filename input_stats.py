def input_stats(inputfile):
    dosya=open(inputfile)
    satirlar=dosya.read().splitlines()
    i=0
    max=0
    sum=0
    for item in satirlar:
        i+=1
        sum+=len(item)
        print("Line",i,"has",len(item),"chars")
        if len(item)>=max:
            max=len(item)
    print(i,"lines; longest = "+str(max)+", average =",sum/i)
    
input_stats("C:\\Users\\90506\\Desktop\\vs code\\2.sınıf1.dönem\\homework2\\carroll.txt")