
file1 = open("mbox.txt", "r")

while(True):
    # read next line
    line = file1.readline()
    # check if line is not null
    if not line:
        break
    # you can access the line
    print(line.strip())

# close file
file1.close
