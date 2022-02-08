marksheet=[[input(),float(input())] for i in range(int(input()))]
marks=list(set(i[1] for i in marksheet))
marks.sort()
ans=[i[0] for i in marksheet if i[1]==marks[1]]
ans.sort()
for i in ans:
    print(i)

# Coded by Shreyash Shrivastava