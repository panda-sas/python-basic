# accepts the user's first and last name and print them in reverse order with a space between them by slicing

f_name = "Jim"
l_name = "Bond"

# print(l_name[::-1] + " " + f_name[::-1])

# using for loop
first_name = ""
last_name = ""
for i in f_name:
    first_name = i + first_name

for j in l_name:
    last_name = j + last_name

print(first_name + " " + last_name)






