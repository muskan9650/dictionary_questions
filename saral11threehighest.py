dict1 = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
from collections import Counter
x = Counter(dict1)
high=x.most_common(3)
for i in high:
        print(i[0]," :",i[1]," ") 


from heapq import nlargest 
ThreeHighest = nlargest(3, dict1, key = dict1.get) 
  
print("Dictionary with 3 highest values:") 
print("Keys: Values") 
  
for val in ThreeHighest: 
    print(val, ":", dict1.get(val)) 


























# max=0
# list1=[]
# max=dict1['a']
# for i in dict1:
#     # print(i)
#     if dict1[i]>max:
#         if max not in list1:
#             max=dict1[i]
#         # if max not in list1:
#             print(max)
#             list1.append(max)
#     # if dict1[i] not in list1:
#     #     print(dict1[i])        
#     # if dict1[i] not in list1:
#     #     if dict1[i]>max:
#     #         max=dict1[i]
#     #     list1.append(max)    
#     print(max)
# print(list1)

