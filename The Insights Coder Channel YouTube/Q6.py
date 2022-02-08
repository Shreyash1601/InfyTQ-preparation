# Coded By Shreyash Shrivastava
string=""
for i in input().split(","):
    name=i.split(":")[0]
    marks=list(map(int,(i.split(":")[1])))
    marks.sort(reverse=True)
    for i in marks:
        if len(name)>=i:
            string+=name[i-1]
            break
    else:
        if len(name)<i:
            string+='X'
print(string)
    