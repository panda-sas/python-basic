# accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

numbers = input("Enter a sequence of comma-separated numbers: ")
list_numbers = numbers.split(",")
tuple_numbers = tuple(list)
print("List :", list_numbers)
print("Tuple :", tuple_numbers)

# accepts a filename from the user and print the extension of that

filename = input("Enter a filename: ")
file_split_values = filename.split(".")
extension_name = file_split_values[-1]
print(extension_name)

# display the first and last colors from the following list

color_list = ["White", "Black", "Red", "Green"]
print("First color is:", color_list[0])
print("Last color is:", color_list[-1])

# accepts an integer (n) and computes the value of n+nn+nnn

a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1+n2+n3)

