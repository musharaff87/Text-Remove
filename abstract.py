import os,glob
folder_path = 'C:/Users/Mohammed Musharaf Z/Desktop/1996-20220822T142548Z-001/1996'
flag = 0
flag2 = 0
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
  with open(filename, 'r') as f:
    text = f.read()
    print(filename)
    string1 = 'abstract'
    string2 = 'introduction'
    file1 = open(filename, "r")

    # setting flag and index to 0
    index = 0


    # Loop through the file line by line
    for line in file1:
      index += 1

      # checking string is present in line or not
      if string1 in line:
        flag = 1
        break
    if(flag):
      index2 = index
    else:
      index2 = 0

        # Loop through the file line by line 22222
    for line in file1:
      index2 += 1

        # checking string is present in line or not
      if string2 in line:
        flag2 = 1
        break

    name,typ = filename.split('.')
    l = len(name) - 2
    v = name[l:]

    print(index)

    print(flag)
    print(flag2)
    print(index2)

    #truncate


    if(v=='v1' or v=='v2' or v=='v3' or v == 'v4' or v=='v5'):
        if(flag==1):
            with open(filename, 'r+') as file:
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
                    if number not in range(index-1, index2-1):
                        file.write(line)

        elif(flag==1 or flag2==1):
            with open(filename, 'r+') as file:
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
                    if number not in range(5, 45):
                        file.write(line)

    else:
      continue