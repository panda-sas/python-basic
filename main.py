# formatting a string at each uppercase letter

sample_string = input("Enter a string: ")
i = 0
for i in range(len(sample_string)):
    if sample_string[i].isupper():
        print(" ")

    # print the sample string
    print(sample_string[i], end='')
