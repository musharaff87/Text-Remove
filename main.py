string1 = '8'
file1 = open("hell", "r")

# setting flag and index to 0
index = 0
flag = 0

# Loop through the file line by line
for line in file1:
    index += 1

    # checking string is present in line or not
    if string1 in line:
        flag = 1
        break

print(index)

with open('hell','r+') as file:
    # read the lines

    lines = file.readlines()
    # move file pointer to the beginning of a file
    file.seek(0)
    # truncate the file
    file.truncate()

    # start writing lines
    # iterate line and line number
    for number, line in enumerate(lines):
        # delete line number 5 and 8
        # note: list index start from 0
        if number not in range(4, 7):
            file.write(line)




