import os
import glob

for modified_data in glob.glob("some/path/to/data/*.csv"):
    content = open(modified_data, 'r').readlines()
    content_modified = open("new/path/" + os.path.basename(modified_data), 'w')

    for i in range(len(content)):
        print("Processing " + modified_data)
        if(content[0].split(' ')[0] == "2"):
            content_modified.write("3" + " " + content[i].split(" ")[1] + " " + content[i].split(" ")[2] + " " 
                            + content[i].split(" ")[3] + " " + content[i].split(" ")[4])
        elif(content[0].split(' ')[0] == "3"):
            content_modified.write("4" + " " + content[i].split(" ")[1] + " " + content[i].split(" ")[2] + " " 
                            + content[i].split(" ")[3] + " " + content[i].split(" ")[4])
        else:
            content_modified.write(content[i].split(" ")[0] + " " + content[i].split(" ")[1] + " " + content[i].split(" ")[2] + " " 
                            + content[i].split(" ")[3] + " " + content[i].split(" ")[4])