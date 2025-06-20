Cricket=["Sushant ", "Ajit", "Nayanesh", "Aditya", "Krunal"]
Badminton=["Ajit", "Aditya", "Krunal", "Varun", "Sachin"]
Football=["Sachin", "Shubham", "Vedant", "Sushant", "Krunal"]
Condition1=[]
for name in Cricket:
    if name in Badminton:
        Condition1.append(name)
print("List of Students who play both Cricket & Badminton:",Condition1)
Condition2=[]
for name in Cricket:
    if name not in Badminton:
        Condition2.append(name)
for name in Badminton :
    if name not in Cricket:
        Condition2.append(name)
print("List of Students who play either Cricket or Badminton but not both:",Condition2)
Condition3=[]
for name in Football:
    if name not in Cricket and Badminton:
        Condition3.append(name)
print("List of Students who nither play Cricket nor Badminton:", Condition3)
print("Number of Students who nither play Cricket nor Badminton:",len(Condition3))
Condition4=[]
for name in Cricket:
    if name in Football:
        if name not in Badminton:
            Condition4.append(name)
print("List of Students who play Cricket and Football but not Badminton:",Condition4)
print("Number of Students who play Cricket and Football but not Badminton:",len(Condition4))




