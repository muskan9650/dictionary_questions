#Write a Python program to sum all the items in a dictionary.
dict1={"a":20, "b":30, "c":40}
sum=0
for key in dict1:
    sum=sum+dict1[key]
print(sum)
