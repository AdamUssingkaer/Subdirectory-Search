import os
import math
import re
TermUser = input("D/S? ")
TermUserNumber = ""
ForbiddenChar = "DS"

DS = ""


while True:
    if "D" in TermUser:
        DS = "Dokumenter"
       
    
    if "S" in TermUser:
        DS = "Sager"
    break

        
else:
    print("Fejl! ikke forventet input")


for char in ForbiddenChar:
    TermUser = TermUser.replace(char,"")
    
FNumber = int(str(TermUser)[:2])
SumNum = int(str(TermUser))

print (FNumber)
print (SumNum)
os.startfile(rf"C:\Users\adamu\OneDrive\Skrivebord\{DS}\{FNumber}\{SumNum}")

  


    



