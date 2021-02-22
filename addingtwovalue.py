#Write a Python program to combine two dictionary adding values for common keys
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
for i in (d1):
    for j in d2 :
        if i==j:
            d = (d1[i] + d2[j])
            d3[i] = d
        elif i>'b' and j>'b':
            d3[i]=d1[i]
            d3[j]=d2[j]
            print(d3)
for a in d3:
    print(d3[a])
            

