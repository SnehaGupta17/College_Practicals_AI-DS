'''
Consider telephone book database of N clients. Make use of a hash table implementation
to quickly look up client‘s telephone number. Make use of two collision handling
techniques and compare them using number of comparisons required to find a set of
telephone numbers
'''
number = []
name = []
n = int(input("Enter table size: "))
for i in range(n):
    name.append(None)
    number.append(None)

def linear_probing():
    for i in range(n):
        nname = input("Enter the name of client: ")
        num = int(input("Enter the telephone number of the client: "))
        hash_val = num % n
        original_hash = hash_val
        while number[hash_val] is not None:
            hash_val = (hash_val + 1) % n
            if hash_val == original_hash:
                print("Table is full. Cannot insert.")
                return
        number[hash_val] = num
        name[hash_val] = nname
        break


def quadratic():
    while True:
        nname = input("Enter the name of the client: ")
        if nname == "":
            break  # Exit if the name is empty
        num = int(input("Enter the telephone number of the client: "))
        hash_val = num % n
        if number[hash_val] is None:
            number[hash_val] = num
            name[hash_val] = nname
        else:
            i = 1
            while True:
                index = (hash_val + i**2) % n
                if number[index] is None:
                    number[index] = num
                    name[index] = nname
                    break
                i += 1


def print_info():
    for i in range(n):
        if name[i] != None:
            print(i, ".", name[i], ":", number[i])

def search(key):
    count = 0
    hash_val = key % n
    while number[hash_val] != None and count < n:
        count += 1
        if number[hash_val] == key:
            print("Key is found")
            print("No. of comparisons to search for the number:", count)
            return
        hash_val = (hash_val + 1) % n
    print("Number is not found")

print("\n1)Linear Probing\n2)Quadratic Probing")
a = int(input("Enter your choice: "))
if a == 1:
    while True:
        print("\n1)Insert client \n2)Print\n3)Search\n4)Exit")
        z = int(input("\nEnter the Operation: "))
        if z == 1:
            linear_probing()
        elif z == 2:
            print_info()
        elif z == 3:
            key = int(input("Enter the key: "))
            search(key)
        else:
            break
else:
    while True:
        print("\n1)Insert client \n2)Print\n3)Search\n4)Exit")
        m = int(input("\nEnter the Operation: "))
        if m == 1:
            quadratic()
        elif m == 2:
            print_info()
        elif m == 3:
            key = int(input("Enter the key: "))
            search(key)
        else:
            break

