import math
n=int(input("number of values"))

l=[]

for item in range(0,n):
    l.append(float(input("enter those values")))

mean=0
for each in range(0,n):
    mean=mean+l[each]

mean=mean/n
print(mean)
temp=[]
sd=0
for item in range(0,len(l)):
    x=(l[item]-mean)*(l[item]-mean)
    temp.append(x/n)

for every in range(0,len(temp)):
    sd=sd+temp[every]



sd=math.sqrt(sd)
print(sd)

a=float(input("assume a value"))


v1=(a-mean)/sd
print(v1)









