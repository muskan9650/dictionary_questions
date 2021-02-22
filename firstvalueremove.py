# Ek program likhiye jo ki nested dictionary me se first key or value ko remove kare.
dic= {
    1: 'NAVGURUKUL',
    2: 'IN',  
  	3:{    
        'A' : 'WELCOME',
        'B' : 'To',
        'C' : 'DHARAMSALA'
        }
    }
dic.pop(dic[3['A']]
print(dic)