list1=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 
list2=[]
for i in range(len(list1)):
    for k in list1[i]:
        if list1[i][k] not in list2:
            list2.append(list1[i][k])
print(list2)