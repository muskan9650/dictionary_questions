#Write a Python program to print all unique values in a dictionary. Go to the editor
list1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# dict1={}
dict1=dict(list1)
print(dict1)
for i in range(len(list1)):
    dict1[i]=list1[i]
print(dict1)

dict1=dict(list1)
print(dict1)