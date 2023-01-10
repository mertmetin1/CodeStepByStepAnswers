

dosya=open("C:\\Users\\90506\\Desktop\\vs code\\2.sınıf1.dönem\\homeworks\\EarthQuakeAreaData.txt","r")
satırlar=dosya.readlines()
names = [0] * len(satırlar)
x_coords = [0] * len(satırlar)
y_coords = [0] * len(satırlar)


for i in range(len(satırlar)):
    SeçilenSatır=satırlar[i]
    SeçilenSatır.split()
    NameXY= SeçilenSatır.split()
   
    names[i]=NameXY[0]
    x_coords[i]=NameXY[1]
    y_coords[i]=NameXY[2]
    
    
print(names)