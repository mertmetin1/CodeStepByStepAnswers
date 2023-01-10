def negative_sum(inputfile):
    dosya=open(inputfile)
    sayilar=dosya.read().split()
    sum=0
    for i in range(len(sayilar)):
        sum+=int(sayilar[i])
        if sum<0:
            break
    if sum<0:
        print(sum,"after",i+1,"steps" )
        return True
    else:
        print("no negative sum")
        return False

    
negative_sum("C:\\Users\\90506\\Desktop\\vs code\\2.sınıf1.dönem\\homework2\\numbers.txt")