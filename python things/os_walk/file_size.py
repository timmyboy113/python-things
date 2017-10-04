print "This is using getsize to see how much every file consumes"
print "---------------"
from os.path import join, getsize
for root, dirs, files in os.walk('/tmp'):
    print root, "consumes",
    print sum([getsize(join(root, name)) for name in files]),
    print "bytes in", len(files), "non-directory files"