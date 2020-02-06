string = "aaabcccdeeeeeeeeeeeffg"
dic = {}

for i in set(string):
    dic[i] = 0
for i in string:
    dic[i] += 1
    

for i in string:
    if dic[i] == 1:
        print(i)
        break
  


    
