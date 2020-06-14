# 2. Get the number of occurrences of var b in array a.
# Example:
# a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
# b = 2
# Result:
# 4

# Global variables my_list and var_to_find used for the list introduced from the keyboard and the item to be counted

my_list = [i for i in input("Please enter the list items : ").split()]
var_to_find = input("Please enter the item you would like to count the occurrences for : ")


occurrences_no = my_list.count(var_to_find)

print("Item", var_to_find, "was found in the array", my_list, "for", occurrences_no, "times")

