records={}
for i in range(int(input())):
    line=input().split()
    name=line[0]
    marks=map(float,line[1:])
    records[name]=marks
query=input()
print('{0:.2f}'.format(sum(records[query])/3))