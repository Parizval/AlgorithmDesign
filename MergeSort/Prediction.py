
#array = list(map(int,input().split()))
array  = [80,100,110,90,65,70,75,90,80,70,100,80,65,60,55,50,100]
#array =  [i for i in  range(10,100,10)]

def NaiveApproach(array):
    sell = 0  
    buy = 0  
    profit = 0
    for i in range(len(array)):
        for  j in range(i+1,len(array)):
            if   array[j] - array[i] > profit:
                profit = array[j] - array[i]
                buy =  array[i]
                sell = array[j]
    print("Buy:{} , Sell: {},Profit: {}".format(buy,sell,profit))

def  Efficient(array):
    buy = array[0] ; profit = 0 ;  sell = array[0] ; extra = array[0]
    for  i in range(1,len(array)):
        if  array[i]  <  buy:
            if  array[i] < extra : 
                extra = array[i]
                #print(array[i])
        if  array[i] - extra >  profit :   
            sell = array[i]
            buy =  extra
            profit = array[i] - extra
    if  profit == 0 :  
        print("No Profit")
        return None
    profit = sell-buy
    print("Buy:{} , Sell: {},Profit: {}".format(buy,sell,profit))

NaiveApproach(array)
Efficient(array)