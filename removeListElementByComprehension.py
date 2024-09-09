limit = int(input("How many number you want to enter in a list "))
print("Enter the values in the list ")
a_list = []
# Loop to take inputs and append them to the list
for i in range(limit):
    element = input(f"Enter element {i+1}: ")
    a_list.append(element)
print(a_list)

num_delete = input("Enter the number you want to delete ")

# Using list comprehension to create a new list without the element to delete
a_list = [item for item in a_list if item != num_delete]
print("Updated list after deletion:", a_list)