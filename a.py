import re ,pprint,os

dir = "D:\\test"

file = os.listdir(dir)
fout = open("list.txt","w")
for f in file:
    print >> fout,"%s" %f

