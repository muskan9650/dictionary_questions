list1=["one", "two", "three", "four", "five"]
list2=[1,2,3,4,5,] 
dict1={}
for i in range(5):
    dict1[list1[i]] = list2[i]
print(dict1)
