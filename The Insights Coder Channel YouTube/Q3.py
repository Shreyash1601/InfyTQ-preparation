# Coded By Shreyash Shrivastava

Input=input("Enter Input")
ans=""
for i in range(1,len(Input),2):
    ans=ans+str(int(Input[i])**2)
    if(len(ans)>=4):
      print(ans[:4])
      break

