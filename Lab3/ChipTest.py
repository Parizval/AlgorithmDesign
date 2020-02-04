import random

def Check(r1,r2):
    number = [-1,1]
    if  r1 + r2 == 2 :  
        return 2 
    elif r1 + r2 == - 2 : 
        return random.choice(number) +  random.choice(number)

    return random.choice(number) - 1

def Recursive(Data,Number):
    number = [0,1]
    Temp =  []
    Id = []

    for i in range(0,len(Data),2):
        if i == len(Data) - 1  :  
            if len(Temp) == 0 :  
                return Data[-1],Id[-1]
                break 
            else:
                continue
        else:
            a  =  random.choice(number)
            Temp.append(Data[i+a])
            Id.append(Number[i+a])
    
    return Temp,Id

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
        
# print(Temp)
# print(Id)

while len(Temp) != 1  : 
    Temp,Id =  Recursive(Temp,Id)


# print(Temp)
# print(Id)


# while len(Temp) !=  1 :
      
#     duplicate  = []
#     Id_duplicate = []

#     for i in range(0,len(Temp),2):
#         if  i == len(TestData) - 1 or i+1 > len(TestData) :  
#             continue
#         if Check(Temp[i],Temp[i+1]) == 2 : 
#         #print(random.choice(number),TestData[i],TestData[i+1])
#             b = random.choice(number)
#             duplicate.append(Temp[i+b])
#             Id_duplicate.append(Id[i+1+b])


#     Temp = duplicate
#     Id =  Id_duplicate
 

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