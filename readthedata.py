
def readthedata(PATH):
    dosya=open(PATH,"r")
    içerik=dosya.readlines()
    average=0
    sum=0
    for i in range(1,len(içerik)):
        Satır=içerik[i].split()
        id=Satır[0]
        vlaue=Satır[1]
        print("id=",id ,"VValue =",vlaue," \n  ")
        sum+=float(vlaue)
    average=sum/len(içerik)
    print("average =",average)
    print("sum =",sum)
    dosya.close()
    
readthedata("C:\\Users\\90506\\Desktop\\vs code\\2.sınıf1.dönem\\homeworks\\data.txt")