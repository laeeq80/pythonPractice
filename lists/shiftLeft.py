limit = int(input("How many numbers do you want to enter in a list? "))
print("Enter the values in the list:")
a_list = []
# Loop to take inputs and append them to the list
for i in range(limit):
    element = int(input(f"Enter element {i+1}: "))
    a_list.append(element)
print("Initial list:", a_list)

# Store the first element in temp
temp = a_list[0]
print("The temp has " + str(temp))

# Shift each element one position to the left
for index in range(limit-1):
    a_list[index] = a_list[index+1]

# Place the first element at the end
a_list[limit-1] = temp

# Print the updated list
print("List after shifting left by one space:", a_list)
