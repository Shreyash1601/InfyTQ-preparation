#Coded By Shreyash Shrivastava

Input=list(map(int,input("Enter Input").split(",")))
num1=sum(Input[:Input.index(4)])+sum(Input[Input.index(7)+1:])
Input2=list(map(str,Input))
num2="".join(Input2[Input2.index('4'):Input2.index('7')+1])
print(num1+int(num2))

