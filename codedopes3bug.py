#Take a list containg only strings. Now, take a string input from user and rearrange the elements of the list according to the number of occurence of the string taken from user in the elements of the list.
#E.g.-LIST : ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
#STRING TAKEN : "bug"
#OUTPUT LIST:["bug bun bug bun bug bug","buggy bug bug buggy","bunny bug","no bun"]

list1 = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
a="bug"
c={}
for i in list1:
    count=0
    for j in i.split():
        if j==a:
            count+=1
    c[count]=i
print(c)
d=[]
for k in sorted(c):
    d.append(c[k])
    d.reverse()
print(d)

