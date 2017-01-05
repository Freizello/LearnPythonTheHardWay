from sys import argv

script, filename = argv #untuk mendapatkan filename

txt = open(filename) #command open untuk buka filename
baca = txt.read()
print "Here's your file %r :"% filename
print baca
#print "Type the filename again : "
#file_again = raw_input ("> ")

#txt_again = open(file_again)

#print txt_again.read()
