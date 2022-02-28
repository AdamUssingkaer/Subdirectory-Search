import os
import math
import re
#Defines different Terms. TermUser is either Dokument or Sager whoich stands for Document or Cases.
#TermUserNumber has no use as of yet
#ForbiddenChar are the TermUser first input, this will be stripped later to replace it with blank so it's only int.
TermUser = input("D/S? ")
TermUserNumber = ""
ForbiddenChar = "DS"

DS = ""

#User chooses between D or S and depending on what they write it will change the state of "DS" to Documents or Cases
while True:
    if "D" in TermUser:
        DS = "Dokumenter"
       
    
    if "S" in TermUser:
        DS = "Sager"
    break

#If user hasn't typed in D or S it will give a error as the program relies on using D or S to know which subdirectory to go to        
else:
    print("Fejl! ikke forventet input")

#Removes D or S so it's only the 4 number combination which is the subdirectory file name in this case
for char in ForbiddenChar:
    TermUser = TermUser.replace(char,"")
 
#FNumber is a subdirectory so if you look for 8243 it will go to subdirectory named "80"
#SumNum is the case file which could be 8243 that is in the "80" subdirectory folder    
FNumber = int(str(TermUser)[:2])
RoundFNumber = round(FNumber/10)*10
SumNum = int(str(TermUser))

print (FNumber)
print (SumNum)
os.startfile(rf"C:\Users\adamu\OneDrive\Skrivebord\{DS}\{RoundFNumber}\{SumNum}")

  


    



