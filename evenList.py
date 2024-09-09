limit = int(input("How many number you want to enter in a list "))
print("Enter the values in the list ")
a_list = []
# Loop to take inputs and append them to the list
for i in range(limit):
    element = int(input(f"Enter element {i+1}: "))
    a_list.append(element)
print(a_list)

a_list = [item for item in a_list if item % 2 == 0]

print(a_list)