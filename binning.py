

l=[13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70]

l.sort()

binn=[]
temp=[]
for item in range(0,len(l),3):
    binn.append(l[item:item+3])
    
print(binn)
mean=[]

for item in range(0,len(binn)):
    temp=binn[item][:]
    mean.append((temp[0]+temp[1]+temp[2])/3)
    
mean1=[]
for every in range(0,len(mean)):
    temp=[mean[every],mean[every],mean[every]]
    mean1.append(temp)
print(mean1)




