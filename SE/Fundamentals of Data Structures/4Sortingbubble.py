marks=[]
n=int(input("enter number of students whose marks are to be displayed:"))
print("Enter marks for",n,"students(press ENTER after every students marks):")
for i in range(0,n):
    ele=int(input())
    marks.append(ele)

def Selection_Sort(marks):
    for i in range(len(marks)):
        min_idx=i
        for j in range(i+1,len(marks)):
            if marks[min_idx]>marks[j]:
                 min_idx=j

        marks[i],marks[min_idx]=marks[min_idx],marks[i]
    print("Marks of students after performing Selection Sort on the list:")
    for i in range(len(marks)):
        print(marks[i])

def Bubble_Sort(marks):
    n=len(marks)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if marks[j]>marks[j+1]:
                marks[j],marks[j+1]=marks[j+1],marks[j]

    print("Marks of students after performing Bubble Sort on the list:")
    for i in range(len(marks)):
        print(marks[i])

def top_five_marks(marks):
    print("Top",len(marks),"Marks are :")
    print(*marks[::-1],sep="\n")
print("The marks of",n,"students are: ")

print(marks)
flag=1;
while flag==1:
    print("1. Selection Sort of the marks")
    print("2. Bubble Sort of the marks")
    print("3. Exit")
    ch=int(input("\n\nEnter your choice(from 1 to 3)"))

    if ch==1:
        Selection_Sort(marks)
        a=input("\nDo you want to display top marks from the list(yes/no) :")
        if a=='yes':
            top_five_marks(marks)
        else:
            print("Jay Ho")
            flag=0

    elif ch==2:
        Bubble_Sort(marks)
        a=input("\nDo you want to display top five marks from the list(yes/no):")
        if a=='yes':
            top_five_marks(marks)

