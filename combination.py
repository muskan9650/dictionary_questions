#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
data = {'1':['a','b'], '2':['c','d']}
for i in data:
    for j in range(2):
        print(data['1'[i]], data['2'[j]])

        # dict1=data['1'][i]*data['2'][j]
        # print(dict1)