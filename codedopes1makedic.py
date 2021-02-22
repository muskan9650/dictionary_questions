# #Ask user to give name and marks of 10 different students. Store them in dictionary.
# dic={}
# i=1
# while i<=3:
#     n=input("enter a key")
#     m=input("enter a value")
#     dic[n]=m
#     i+=1
# print(dic)
# #Sort the dictionary created in previous example according to marks.
# import operator
# d1=dict(sorted(dic.items(),key=operator.itemgetter(1)))
# print(d1)

l=65
i=1
while i<4:
    b=i
    while b<=3:
        print(" ", end="")
        b+=1
    n=i
    while n==1:
        print(chr(l),i, chr(l))
        n=n+1
    c=1
    n=l
    while c<=i:
        print(chr(n),c,end="")
        c=c+1
        n=n+1
    d=i+1
    k=l+d
    while d>0:
        print( chr(k),d,end="")
        d=d-1
        k=k-1
    print()
    i+=1
    