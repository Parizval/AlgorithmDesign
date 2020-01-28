import random

def Check(r1,r2):
    return r1 +  r2

TestData =  [-1,-1,-1,1,1,1,1,1,1,1]

number = [0,1]
Temp = []
Id = []
for i in range(0,len(TestData),2):
    if  i == len(TestData) - 1  :  
        continue
    if Check(TestData[i],TestData[i+1]) == 2 : 
        #print(random.choice(number),TestData[i],TestData[i+1])
        a  =  random.choice(number)
        Temp.append(TestData[i+a])
        Id.append(i+1+a)
        

while len(Temp) !=  1 :
    i = 0  
    duplicate  = []
    Id_duplicate = []

    
    if Check(Temp[i],Temp[i+1]) == 2 : 
        #print(random.choice(number),TestData[i],TestData[i+1])
        b = random.choice(number)
        duplicate.append(Temp[i+b])
        Id_duplicate.append(Id[i+1+b])


    Temp = duplicate
    Id =  Id_duplicate
    i +=  2  

print("{} th Robot is correctly identified. \n".format(Id[0]))

index = Id[0] - 1 
for i in range(len(TestData)):
    if  i == index : 
        continue
    else:   
        if Check(TestData[index],TestData[i]) == 2 :  
            print("{}th Robot is working fine.".format(i+1))
        else:
            print("{}th Robot is malfunctioning.".format(i+1))