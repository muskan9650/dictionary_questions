# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) 
# in the form (x, x*x). Go to the editor
n=int(input("enter a number"))
dic={}
for x in range(1, n+1):
    dic[x]=x*x
print(dic)

