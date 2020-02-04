n = int(input("Enter the Weight(in tonne): "))
ans  = 0 

while n != 0 :  
    if  n >=  25 : 
        ans  += 1 
        n += -25
        
    elif n >=  10 : 
        ans  += 1 
        n += -10
    elif n >=  5 : 
        ans  += 1 
        n += -5
    else:
        ans += n 
        break
    
print("Number of Trucks: {}".format(ans))
    
