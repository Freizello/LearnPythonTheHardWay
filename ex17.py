from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

#Coba bikin jadi 1 baris
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" %exists(to_file)

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, Copying done."

out_file.close()
open(from_file).close()
