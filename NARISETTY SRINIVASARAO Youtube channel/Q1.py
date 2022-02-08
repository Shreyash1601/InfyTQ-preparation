# Coded By Shreyash Shrivastava

import re
string=input()
alphabets=(re.findall(r"[a-zA-Z]",string))
alphabets.reverse()
for i in range(len(string)):
    if not string[i].isalpha():
        alphabets.insert(i,string[i])
print("".join(alphabets))