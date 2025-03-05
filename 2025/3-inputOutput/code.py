with open("users.txt") as file_obj:
    contents = file_obj.read()
    print(contents)

##################################

with open("users.txt") as file_obj:
    contents = file_obj.readlines()
    print(contents)

##################################

def file_read(infile):
    with open(infile,'r') as reading:
        li = []
        for i in reading:
            li.append(i)
        for j in li:
            print(j, end='\n')

file_read("file1.txt")

##################################

def copy_paste(infile, outfile):
    with open(infile) as infile_obj:
        infile_content = infile_obj.read()
    with open(outfile, "w") as outfile_obj:
        for i in infile_content:
            outfile_obj.write(i)

copy_paste("file1.txt","outfile.txt")

##################################

def linenums(inpath, outpath):
    with open(inpath) as inpath_obj:
        li = []
        for i in inpath_obj:
            li.append(i)
    with open(outpath, "w") as outpath_obj:
        num = 1
        for i in li:
            outpath_obj.write(str(num) + ': ' + i)
            num += 1

linenums("users.txt","outfile.txt")