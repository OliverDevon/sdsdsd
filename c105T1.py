import csv, math
with open('data105.csv')as f:
    reader=csv.reader(f)
    filelist=list(reader)
data=filelist[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+int(x)
    mean = total/n
    return mean
squarelist=[]
for o in data:
    a=int(o)-mean(data)
    a=a**2
    squarelist.append(a)
sum=0
for i in squarelist:
    sum+=i
reasult=sum/(len(data)-1)
sd=math.sqrt(reasult)
print(sd)
