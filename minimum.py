#Write a Python program to get the maximum and minimum value in a dictionary. 
dict1={"sam":20, "muskan":40, "sachin":50, "preeti":10}
min=dict1["sam"]
for x in dict1:
    if min > dict1[x]:
        min = dict1[x]
print(min)
