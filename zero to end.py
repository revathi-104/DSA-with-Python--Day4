#move all zeros to end
#input: [0,1,0,3,12]
#output: [1,3,12,0,0]
arr=[0, 1, 0, 3, 12]
temp=0
new_arr=[]
for i in arr:
    if i==0:
        temp+=1
    else:
        new_arr.append(i)
for i in range(temp):
    new_arr.append(0)
print(new_arr)