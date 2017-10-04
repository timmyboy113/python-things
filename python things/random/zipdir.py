import zipfile
import os

z = zipfile.ZipFile('my-archive.zip', 'w', zipfile.ZIP_DEFLATED)
startdir = "C:\Users\Bexlie\SkyDrive\Bilder\blender test"
for dirpath, dirnames, filenames in os.walk(startdir):
  for filename in filenames:
    z.write(os.path.join(dirpath, filename))
z.close()