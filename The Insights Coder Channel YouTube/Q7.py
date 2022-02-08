# Coded By Shreyash Shrivastava

for i in input().strip().split(','):
    name=i.strip().split(":")[0]
    marks=list(map(int,(i.split(":")[1])))
    SquareSum=sum(map(lambda i:i**2,marks))
    if SquareSum%2==0:
        print(name[len(name)-2:]+name[:len(name)-2])
    else:
        print(name[1:]+name[0])

