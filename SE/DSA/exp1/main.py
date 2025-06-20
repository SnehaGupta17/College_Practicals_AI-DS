from LinearProbing import hashTable
from Record import Record
from DoubleHashing import doubleHashTable

def input_record():
    record = Record()
    record.set_name(input("Enter Name:"))
    record.set_number(int(input("Enter Number:")))
    return record

def handle_operations(hash_table):
    while True:
        print("************************")
        print("1. Insert              *")
        print("2. Search              *")
        print("3. Display             *")
        print("4. Back                *")
        print("************************")

        choice = int(input("Enter Choice:"))
        if choice == 1:
            hash_table.insert(input_record())
        elif choice == 2:
            hash_table.search(input_record())
        elif choice == 3:
            hash_table.display()
        elif choice == 4:
            break
        else:
            print("Please Enter Valid Choice")

while True:
    print("************************")
    print("1. Linear Probing      *")
    print("2. Double Hashing      *")
    print("3. Exit                *")
    print("************************")

    choice = int(input("Enter Choice:"))
    if choice == 1:
        handle_operations(hashTable())
    elif choice == 2:
        handle_operations(doubleHashTable())
    elif choice == 3:
        break
    else:
        print("Please Enter Valid Choice")
