#HarvardX CS50

#PSET-1 

#DEEP THOUGHT

import operator


Ft=input("what is the universe?")

if Ft=="42":
    print("yes")
elif Ft=="forty two":
    print("yes")
elif Ft=="forty-two":
    print("Yes")
else:
    print("wrong number")

#HOME FEDERAL SAVING

gr=input("input your greeting\n")
gr=gr.lower()

if gr =="hello":
    print("$0")
elif gr=="hey":
    print("$20")
elif gr=="hi":
    print("$20")
elif gr=="howdy":
    print("$20")
elif gr=="how are you":
    print("$20")
else:
    print("$100")

#FILE EXTENSIONS

file=str(input("enter your file name to check extensions\n"))

if ".gif" in file:
    print("GIF file")

elif ".jpg" in file:
    print("JPEG file")

elif ".jpeg" in file:
    print("JPEG file")

elif ".png" in file:
    print("PNG file")

elif ".pdf" in file:
    print(" PDF file")

elif ".txt" in file:
    print("TXT file")

elif ".zip" in file:
    print("ZIP file")

else:
    e="application/octet-stream"
    print(e)

#MATH INTERPRETER



#MEAL TIME


