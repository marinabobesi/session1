# 1. Reverse the order of the items in an array.
# Example:
# a = [1, 2, 3, 4, 5]
# Result:
# a = [5, 4, 3, 2, 1]


# Global variable my_list used for the list introduced from the keyboard

my_list = [int(i) for i in input("Please enter the  integer numbers separated by space forming th list you would like to reverse : ").split()]

# 5 different methods defined for reversing the items in an array

# 1.Using reverse() function


def list_reversing_reverve(my_list):
    print ("Reversing a list using reverse function \nInitial list:", my_list)
    my_reversed_list = my_list.copy()
    my_reversed_list.reverse()
    print ("Reversed list:", my_reversed_list, "\n")

# 2. Using reversed() function


def list_reversing_reversed(my_list):
    print ("Reversing a list using reversed function \nInitial list:", my_list)
    my_list=(list(reversed(my_list)))
    print ("Reversed list:", my_list, "\n")

# 3. Using slicing


def list_reversing_slicing(my_list):
    print ("Reversing a list using slicing \nInitial list:", my_list)
    my_list = my_list[::-1]
    print ("Reversed list:", my_list, "\n")

# 4. Doubling the list elements


def list_reversing_doubling(my_list):
    print ("Reversing a list by doubling it and swapping \nInitial list:", my_list)
    my_list_length = int(len(my_list))
    my_list = my_list * 2
    for i in range(0,my_list_length):
        my_list[i]=my_list[-i-1]
    del my_list[-my_list_length:]
    print ("Reversed list:", my_list, "\n")

# 5. Using swap


def list_reversing_swapping(my_list):

    print ("Reversing a list with swapping algorithm \nInitial list:", my_list)
    my_list_length = len(my_list)
    highest_index = my_list_length - 1
    iterations = int(my_list_length/2)

    for i in range(0, iterations):
        temp_var = my_list[highest_index]
        my_list[highest_index] = my_list[i]
        my_list[i] = temp_var
        highest_index -= 1
    print ("Reversed list:", my_list, "\n")

# Defining main function


def main():
    list_reversing_reverve(my_list)
    list_reversing_reversed(my_list)
    list_reversing_slicing(my_list)
    list_reversing_doubling(my_list)
    list_reversing_swapping(my_list)

# Calling main function


main()
