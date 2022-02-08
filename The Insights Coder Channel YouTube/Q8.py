# Coded By Shreyash Shrivastava
Input=input("Enter string")
mid=len(Input)//2
for i in range(mid,0,-1):
    prefix=Input[0:i]
    suffix=Input[len(Input)-i:len(Input)]
    if(prefix==suffix):
        print(len(prefix))
        break;
    