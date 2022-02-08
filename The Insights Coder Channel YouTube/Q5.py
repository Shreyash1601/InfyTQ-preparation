# Coded By Shreyash Shrivastava
stack=[]
cnt=0
for i in list(input("Enter string")):
    if i in{'(','{','['}:
        stack.append(i)
        cnt+=1
        continue
    elif (len(stack)==0):
        print(cnt+1)
        exit()
    b=stack.pop()
    if i==')' and b=='(':
        cnt+=1
    elif i=='}' and b=='{':
        cnt+=1
    elif i==']' and b=='[':
        cnt+=1
if(len(stack)==0):
    print(0)
else:
    print(cnt+1)