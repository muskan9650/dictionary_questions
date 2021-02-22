#Write a Python program to get the maximum and minimum value in a dictionary. 
dict1={"sam":20, "muskan":40, "sachin":50, "preeti":10}
max=dict1["sam"]
for value in dict1:
    if max<dict1[value]:
        max = dict1[value]
print(max)
   