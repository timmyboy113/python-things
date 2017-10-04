print '''
   BY BELINE
   '''
   
datei = raw_input("Welche datei?")
print "Es wird versucht ", datei," zu Laden ..."
d = open(datei,"w+")
print "Name of the file: ", d.name
print d.name, "wurde erfolgreich geladen"

for index in range(3):    
#     line = d.next()
#     print "Line No %s - %s" % (index, line)
      print index


d.close()