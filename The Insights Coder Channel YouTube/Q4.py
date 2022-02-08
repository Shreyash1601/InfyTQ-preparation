# Coded By Shreyash Shrivastava

Input=[i for i in (set([i for i in input("Enter string") if i.isdigit()==True]))]
Input.sort(reverse=True)
Number=''.join(Input)
if(int(Number)%2==0):
    print(Number)
else:
    for i in range(len(Number)-1,0,-1):
        if(int(Number[i])%2==0):
            a=Number[i]
            Input.remove(a)
            Input.insert(len(Number)-1,a)
            print(''.join(Input))
            break
    else:
        print(-1)