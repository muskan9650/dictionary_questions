dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball": "green",
    "bat":3
    } 
dic2={}
for i in dic:
    if i not in dic2:
        dic2[i]=dic[i]
print(dic2)  
