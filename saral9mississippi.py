a="MISSISSIPPI"
list1=list(a)
print(list1)
list2=[]
dict1={}
for i in range(len(a)):
    count=1
    for j in range(i+1, len(a)):
        if list1[i] not in list2:
            list2.append(list1[i])
for i in range(len(list2)):
    count=0
    for j in range(len(list1)):
        if list2[i]==list1[j]:
            count=count+1
    print(list2[i],count)
    dict1[list2[i]]=count
print(dict1)
