# name = input("What's your name? ")

# opening the file I would like to store information in
# name could be anything I prefer
# w for write

# second argument w for write
# tell open to open the file in a way that I would like to change
# if the file doesn't exist, w will create it for you

# caution: w will recreate the file everytime it is accessed


# with open("names.txt", "a") as file:
#    file.write(f"{name}\n")

# file.close()

# r == read file
# with open("names.txt", "r") as file:
    # read all the lines in the file and store it in a variable called lines
    # lines = file.readlines()

# for line in lines:
    # print("hello,", line.rstrip())

# with open("names.txt", "r") as file:
    # for line in file:
        # print("hello,", line.rstrip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

