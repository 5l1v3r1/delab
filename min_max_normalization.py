

l=[]

n=int(input("enter number of values"))

for item in range(0,n):
    l.append(float(input("enter values")))

l.sort()
print(l)

v=float(input("assume a value"))    


min1=l[0]
max1=l[-1]

v1= ((v-min1)/(max1-min1))*(1-0)
v1_new=v1+0

print(v1_new)
