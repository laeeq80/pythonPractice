import sys

List = [2,54,67,34,23,78]
number= int(input("Enter the value you want to search\n"))
for value in List:
    if number == value:
        print ("Element found at location " + str(List.index(value)))
        sys.exit()

print('Element not found in the List')