str = input()
x_count = o_count = 0

for i in range(len(str)):
    if str[i]=='x':x_count+=1
    else:o_count+=1

if x_count==o_count:print(True)
else:print(False)
