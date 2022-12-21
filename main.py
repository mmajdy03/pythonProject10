#السؤال الاول


print("enter name and age and addrass")
name=input()
age=input()
address=input()
if name=="":
    print("the input is erorr")
else:
   print("the name is string",not(name.isdigit()))
   print("the age is int:",age.isdigit())
   print("hello mr/ms",{name}," age",{age}," located in",{address},".")
   print("thanks for beening one of our community \t Enjoy")



# السؤال الثاني
from math import *
a=input("enter the number1>")
a=int(a)
b=input("enter the number2>")
b=int(b)
z=0

oprat=input("enter the number oprat\n"
      "1_+\n"
      "2_ -\n"
      "3_ *\n"
      "4_ /\n"
      "5_ ^\n"
      "6_ %\n"
            ">")
if oprat.isdigit():
    oprat = int(oprat)
    c=""
if oprat==1 or oprat=='+':
    z=a+b
    c="+"
elif oprat==2:
    z=a-b
    c = "-"
elif oprat==3:
    z=a*b
    c = "*"
elif oprat==4:
    z=a/b
    c = "/"
elif oprat==5:
    z=a^b
    c = "^"
elif oprat==6:
    z=a%b
    c = "%"
else:print("erorr:enter the number correct")
print(z)
oprat2=input("enter the num oprat\n"
             "1_ceil or floor or round\n"
             "2_ without a decimal point\n"
             "3_Exit\n"
             ">>>>>>")
oprat2=int(oprat2)
if oprat2==1:
    oprat2=input("enter the num oprat\n"
                 "1_cill\n"
                 "2_floor\n"
                 "3_round\n"
                 ">>>>")
    oprat2=int(oprat2)
    if oprat2==1:
        z=ceil(z)
    elif oprat2==2:
        z=floor(z)
    else:
        z=round(z)
elif oprat2==2:
    z=int(z)
else:
    print("exit")
print(a,c,b,'=',z)




# السؤال الثالث

x=[]
x.append(input("enter 1 number>>"))
x.append(input("enter 2 number>>"))
x.append(input("enter 3 number>>"))
x.append(input("enter 4 number>>"))
x.append(input("enter 5 number>>"))
x.sort()
max=x[4]
min=x[0]
print("the max is :",max)
print("the min is :",min)

