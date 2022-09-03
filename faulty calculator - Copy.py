#faulty calculator 

print("Enter your first number")
var1=int(input())
print("Enter the operator")
word3=(input())
print("Enter your second number")
var2=int(input())

if var1==45 and  word3=="*" and var2==3:
    print("Answer is 555")

elif var1==56 and word3=="+" and var2==9  :
 print("Answer is 77")

elif var1==56 and  word3=="/" and var2==6 :
 print("Answer is 4")

elif word3=="*" :
    print("Answer is")
    print(var1*var2)


elif word3=="+" :
    print(var1+var2)

elif word3=="/" :
    print(var1/var2)

