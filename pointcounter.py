dosya= open("C:\\Users\\90506\\Desktop\\vs code\\2.sınıf1.dönem\\homeworks\\points.txt","r")

satır= dosya.readline()
students=[0]*5
for i in range(len(satır)):
        if satır[i]=="y":
            students[i%5]+=3
        if satır[i]=="n":
            students[i%5]+=1
        students[i%5]+=0
        
for k in range(len(students)):
    print("student ",k+1,"'s point =",students[k])    
            
            


dosya.close()

