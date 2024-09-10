limit = int(input("How many numbers do you want to enter in the list? "))
print("Enter the values in the list:")
a_list = []
# Loop to take inputs and append them to the list
for i in range(limit):
    element = int(input(f"Enter element {i+1}: "))
    a_list.append(element)
print("Initial list:", a_list)

# Input: Number of positions to shift left
shift = int(input("How many positions do you want to shift left? "))

# Ensure the shift value is within bounds by taking modulo
shift = shift % limit

# Shift the list using slicing
# a_list[shift:] takes the part of the list starting from the shift index to the end.
# a_list[:shift] takes the first shift elements of the list.
# two parts are then concatenated to form the rotated list
a_list = a_list[shift:] + a_list[:shift]

# Print the updated list
print("List after shifting left by", shift, "positions:", a_list)