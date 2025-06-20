def DeleteDuplicates(Books):
    #Deleting duplicate Entrise
    Final_Books_List=[]
    for num in Books:
        if num not in Final_Books_List:
            Final_Books_List.append(num)
    print("On removing Duplicates")
    print(Final_Books_List)
    
def Sorting(Books,N):
    #Sorting in Ascending Order
    for i in range(N):
        for j in range (i+1,N):
            if (Books[i][1]>Books[j][1]):
                temp1=Books[i][0]
                Books [i][0]=Books[j][0]
                Books [j][0]=temp1
                
                temp2=Books[i][1]
                Books[i][1]=Books[j][1]
                Books[j][1]=temp2
                
    print("The Books are:")
    print(Books)
    
def MoreCost(Books,N):
    cnt=0
    for isbn in range(N):
        if (Books[isbn][1]>500):
            cnt=cnt+1
    print("Number of Books having cost more than 500 are:",cnt)
     
def LessCost(Books,N):
    cnt=0
    for isbn in range(N):
        if (Books[isbn][1]<500):
               cnt=cnt+1
    new_List=[[0 for cost in range(2)]for isbn in range(cnt)]
    for isbn in range(N):
        if (Books[isbn][1]<500):
            new_List[isbn][0]=Books[isbn][0]
            new_List[isbn][1]=Books[isbn][1]
        print("\n Books having the cost less than 500 are follow:")
        print("\n  ISBN \t Cost")
        for isbn in range(cnt):
            print(" ",new_List[isbn][0],"\t",new_List[isbn][1])
            

N=int(input("enter number of books"))
Books=[[0 for cost in range(2)] for isbn in range(N)]
for isbn in range (N):
    ISBN=int(input("enter the ISBN:"))
    Books[isbn][0]=ISBN
    COST=int(input("enter the cost:"))
    Books [isbn][1]=COST
print("The Books are:")
print(Books)
while(True):
    print("\n DY Patil Department Library Books Demo")
    print("\n 1. Delete Duplicate Entries")
    print("2.Display Books in Ascending Order based on cost books")
    print("3.Display total Number of Books with cost more than 500")
    print("4.Display new list which has cost less than 500")
    print("5.Exit.")
    print()
    
    choice =int(input("Enter your choice"))
    if (choice==1):
        DeleteDuplicates(Books)
    elif (choice==2):
        Sorting(Books,N)
    elif(choice==3):
        MoreCost(Books,N)
    elif(choice==4):
        LessCost(Books,N)
    else:
        print("Exit.")
        break
        
        
