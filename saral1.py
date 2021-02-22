d1={1:10, 2:20}
d2={3:30, 2:20}
d3={5:50, 6:60}
d4={}
for i in (d1):
    print(i)
    for j in d2 :
        if i==j:
            d = (d1[i]+d2[j])
            d4[i] = d
        else:
            d4[i]=d1[i]
            d4[j]=d2[j]
    d4.update(d3)
print(d4)

