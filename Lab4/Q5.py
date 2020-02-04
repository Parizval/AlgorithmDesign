k = int(input("Enter the Weight: "))
array = list(map(int,input("Enter size of truck: ").split()))

array.append(1)
ans = 0 
n = k 
for i in  range(n):
    temp = array[0]
    for j in array:
        if  temp > k :  
            if j <  k : 
                temp = j 
            continue
        if j <= k and  j > temp: 
            temp = j  
    
    k -= temp
    #print(temp)
    ans += 1  
    if  k <= 0  :  
        break
print("Number of trucks: {}".format(ans))