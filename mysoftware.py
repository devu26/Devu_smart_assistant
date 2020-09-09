print("enter 1 for chrome ,enter 2 for notepad")
print("enter your choice:" ,end='')
p=input()
import os
if int(p)==1:
 os.system("chrome")
elif int(p)==2:
 os.system("notepad")
else :
 print("not support")
print("thank u")