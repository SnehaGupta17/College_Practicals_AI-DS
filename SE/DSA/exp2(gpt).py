class Set:
    # Creates an empty set instance.
    def __init__(self, initElementsCount):
        self._s = []
        for i in range(initElementsCount):
            e = int(input("Enter Element {}: ".format(i + 1)))
            self.add(e)

    def get_set(self):
        return self._s

    def __str__(self):
        string = "\n{ "
        for i in range(len(self.get_set())):
            string = string + str(self.get_set()[i])
            if i != len(self.get_set()) - 1:
                string = string + " , "
        string = string + " }\n"
        return string

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._s)

    # Determines if an element is in the set.
    def __contains__(self, e):
        return e in self._s

    # Determines if the set is empty.
    def isEmpty(self):
        return len(self._s) == 0

    # Adds a new unique element to the set.
    def add(self, e):
        if e not in self:
            self._s.append(e)

    # Removes an e from the set.
    def remove(self, e):
        if e in self.get_set():
            self.get_set().remove(e)

    # Determines if this set is equal to setB.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for e in setB.get_set():
            if e not in self.get_set():
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = self
        for e in setB:
            if e not in self.get_set():
                newSet.add(e)
        return newSet

    # Creates a new set from the intersection: self set and setB.
    def intersect(self, setB):
        newSet = Set(0)
        for i in range(len(self.get_set())):
            for j in range(len(setB.get_set())):
                if self.get_set()[i] == setB.get_set()[j]:
                    newSet.add(self.get_set()[i])
        return newSet

    # Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        newSet = Set(0)
        for e in self.get_set():
            if e not in setB.get_set():
                newSet.add(e)
        return newSet

    # Creates the iterator for traversing the list of items
    def __iter__(self):
        return iter(self._s)

def createSet():
    n = int(input("Enter number of Elements in set: "))
    s = Set(n)
    return s


print("Create Set A:")
s1 = createSet()
print("Set A:", str(s1))

print("\nCreate Set B:")
s2 = createSet()
print("Set B:", str(s2))

while True:
    print("\n|-------------------|")
    print("| Menu              |")
    print("| 1. Add            |")
    print("| 2. Remove         |")
    print("| 3. Contains       |")
    print("| 4. Size           |")
    print("| 5. Intersection   |")
    print("| 6. Union          |")
    print("| 7. Difference     |")
    print("| 8. Subset         |")
    print("| 9. Exit           |")
    print("|-------------------|")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        set_choice = input("Enter Set (A/B) to Add Element: ")
        if set_choice.upper() == 'A':
            e = int(input("Enter Number to Add to Set A: "))
            s1.add(e)
            print("Set A:", str(s1))
        elif set_choice.upper() == 'B':
            e = int(input("Enter Number to Add to Set B: "))
            s2.add(e)
            print("Set B:", str(s2))
        else:
            print("Invalid set choice!")

    elif choice == 2:
        set_choice = input("Enter Set (A/B) to Remove Element: ")
        if set_choice.upper() == 'A':
            e = int(input("Enter Number to Remove from Set A: "))
            s1.remove(e)
            print("Set A:", str(s1))
        elif set_choice.upper() == 'B':
            e = int(input("Enter Number to Remove from Set B: "))
            s2.remove(e)
            print("Set B:", str(s2))
        else:
            print("Invalid set choice!")

    elif choice == 3:
        set_choice = input("Enter Set (A/B) to Search Element: ")
        if set_choice.upper() == 'A':
            e = int(input("Enter Number to Search in Set A: "))
            if e in s1:
                print("Number Present in Set A")
            else:
                print("Number is not Present in Set A")
            print("Elements of Set A:", str(s1))
        elif set_choice.upper() == 'B':
            e = int(input("Enter Number to Search in Set B: "))
            if e in s2:
                print("Number Present in Set B")
            else:
                print("Number is not Present in Set B")
            print("Elements of Set B:", str(s2))
        else:
            print("Invalid set choice!")
 
    elif choice == 4:
        set_choice = input("Enter Set (A/B) to Get Size and Elements: ")
        if set_choice.upper() == 'A':
            print("Set A Contains {} elements:".format(len(s1)))
            print("Elements of Set A:", str(s1))
        elif set_choice.upper() == 'B':
            print("Set B Contains {} elements:".format(len(s2)))
            print("Elements of Set B:", str(s2))
        else:
            print("Invalid set choice!")

    elif choice == 5:
        s3 = s1.intersect(s2)
        print("Intersection of Set A and Set B:", str(s3))

    elif choice == 6:
        s3 = Set(0)
        for elem in s1:
            s3.add(elem)
        for elem in s2:
            s3.add(elem)
        print("Union of Set A and Set B:", str(s3))

    elif choice == 7:
        s3 = s1.difference(s2)
        print("Difference of Set A and Set B:", str(s3))

    elif choice == 8:
        if s1.isSubsetOf(s2):
            print("Set A is a Subset of Set B")
        else:
            print("Set A is not a Subset of Set B")

    elif choice == 9:
        break

    else:
        print("Please Enter Valid Choice")
