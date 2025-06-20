import array as arr


# Accept the % marks of the students

def accept_perc():
    a = arr.array('f', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(float(input("Enter the First Year % of Student[{0}] : ".format(i))))
    return a


# Print the % marks of the Students

def print_perc(a):
    for i in range(0, len(a)):
        print("\t {0:.2f}".format(a[i]), end=" ")
    print()


# Shell Sort

def shell_sort(a):
    # Start with a big gap, then reduce the gap
    n = len(a)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = a[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap

                # put temp (the original a[i]) in its correct location
            a[j] = temp
        gap //= 2
    return a


# Insertion sort

def ins_sort(a):
    # Traverse through 1 to len(a)
    for i in range(1, len(a)):

        key = a[i]

        # Move elements of a[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# Top 5 Score

def top_five(a):
    print("Top five score are : ")
    cnt = len(a)

    if cnt < 5:
        start, stop = cnt - 1, -1  # stop set to -1 as we want to print the 0th element
    else:
        start, stop = cnt - 1, cnt - 6

    for i in range(start, stop, -1):
        print("\t {0:.2f}".format(a[i]), end=" ")


# Driver program
if __name__ == "__main__":

    unsort_A = arr.array('f', [])
    ins_sort_A = arr.array('f', [])
    shell_sort_A = arr.array('f', [])
    flag = 1

    while flag == 1:
        print("\n 1. Accept array elements \n 2. Display the Elements \n 3. Insertion Sort \n 4. Shell Sort \n 5. exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_perc()

        elif choice == 2:
            print_perc(unsort_A)

        elif choice == 3:
            print("Elements after sorting using Insertion Sort :")
            ins_sort_A = ins_sort(unsort_A)
            print_perc(ins_sort_A)
            top_five(ins_sort_A)

        elif choice == 4:
            print("Elements after sorting using Shell Sort :")
            shell_sort_A = shell_sort(unsort_A)
            print_perc(shell_sort_A)
            top_five(shell_sort_A)

        else:
            print("Wrong choice")
            flag = 0

