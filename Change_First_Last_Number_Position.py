lenght_value=int(input("ededinizin reqemlerinin sayini daxil edin:"))

m=1

value_list=[]
value_index=[]

while m<=lenght_value:
    value=int(input("ededin bir reqemini yazdiqdan sonra enter duymesine sixin:"))
    value_list.append(value)
    m+=1

if lenght_value==1:
    print("Xahis olunur 2 ve daha cox reqemli eded daxil edin!")

else:
    for s in value_list:
        index=value_list.index(s)
        value_index.append(index)

    max_index=max(value_index)
    value_index.remove(0)
    value_index.remove(max_index)
    process_end=[value_list[max_index],value_list[0]]
    
    for s in value_index:
        process_end.insert(s,value_list[s])

    for s in process_end:
        print(s,end="")
        
        
        
    
