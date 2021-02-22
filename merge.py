#Write a Python script to merge two Python dictionaries.
dict1={"muskan":30, "rahul":40, "manisha":50}
dict2={1:"swati", 2:"reena", 3:"moni"}
dict3={}
for x in (dict1,dict2):
    dict3.update(x)
print(dict3)