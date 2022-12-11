import os,glob
folder_path = 'C:/Users/Mohammed Musharaf Z/Desktop/1996-20220822T142548Z-001/1996'
flag = 0
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
  with open(filename, 'r') as f:
    text = f.read()
    print(filename)
    string1 = 'references'
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
    name,typ = filename.split('.')
    l = len(name) - 2
    v = name[l:]

    print(index)

    #truncate
    if(v=='v1' or v=='v2' or v=='v3' or v == 'v4' or v=='v5'):
      if(flag):
        with open(filename, 'r+') as file:
          # read the lines
          lines = file.readlines()

          # move to the top of the file
          file.seek(int(index))
          file.truncate()

          file.writelines(lines[0:index - 1])

        with open(filename, 'r') as file:
          lines = file.readlines()

        for line in lines:
          print(line)

      else:
        continue

    else:
      continue