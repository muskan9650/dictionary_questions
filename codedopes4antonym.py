#Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words
# and then ask user to enter a word and display antonym of it.
dic1={'up':'down', 'right':'left','yes':'no', 'beautifull':'ugly', 'true':'false'}
for i in dic1:
    print(i)
n=input("enter a word")
if n in dic1.keys():
    print(n," : ", dic1[n])
else:
    print("type correct word")


