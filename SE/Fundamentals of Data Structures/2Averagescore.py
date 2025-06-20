# Function for average score of the class
def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-1:
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    print("Total Marks : ", sum)
    print("Average Marks :", avg)
def Maximum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-1:
            Max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max)
def Minimum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-1:
            Min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)
def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-1:
            count+=1
    return(count)
def maxFrequency(listofmarks):
    i=0
    Max=0
    print(" Marks | Frequency")
    for j in listofmarks:
        if (listofmarks.index(j)==i):
            print(j," | ",listofmarks.count(j))
            if listofmarks.count(j)>Max:
                Max=listofmarks.count(j)
                mark=j
    i=i+1
    return(mark,Max)
marksinFDS=[]
numberofstudents=int(input("Enter total number of students : "))
for i in range(numberofstudents):
    marks=int(input("Enter marks of student : "))
    marksinFDS.append(marks)
average(marksinFDS)
print("\n maximum ==",Maximum(marksinFDS))
print("\n Minimum ==",Minimum(marksinFDS))
print("\n No of student absent ==",absentcount(marksinFDS))
print("\n max Frequency ==",maxFrequency(marksinFDS))