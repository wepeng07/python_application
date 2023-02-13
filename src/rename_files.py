# Run this script from the repository's root.
import re
import os


def rename(path):
    files = os.listdir(path)
    sort_files = []
   
    for file in files:
        if os.path.isdir(file): continue
        a = re.findall('(?<=snap).*?(?=.txt)',file)
        if len(a) != 0:
            sort_files.append(file)
   
    sort_files.sort(key= lambda x:int(x[-7:-4]))
    prev = 1        
    for file in sort_files:
        print(file)
        a = re.findall('(?<=snap).*?(?=.txt)',file)
        last = int(a[0])
        if last > prev:
            os.rename(path+file,path+"snap"+"%03d" % prev+".txt")
        prev+=1




