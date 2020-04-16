from __future__ import absolute_import, division, print_function
from __future__ import  unicode_literals


import zipfile, time
import sys, os
import subprocess




tm = time.strftime("%Y_%m_%d_%H_%M")

filename = r'Miniproject_%s.zip' % tm


source = r"dist\miniproject-0.0.1.zip"

zip_path = os.path.join('backup', filename)

backup_dir = r"E:\AlterPC\projects\Miniproject\backup"





if __name__ == '__main__':
    if os.path.exists(source):
        os.remove(source)

    subprocess.check_output([sys.executable, "setup.py", "sdist", "--format=zip"]) 
    subprocess.check_output(["cmd", "/c", "copy", source, zip_path]) 
    try:
        print( subprocess.check_output(["cmd", "/c", "copy", zip_path, backup_dir]) )
        zf = zipfile.ZipFile(os.path.join(backup_dir, os.path.join(backup_dir,filename)))
        print ("Backup to external drive successful!")
    except:
        print ("Backup to external drive did not work!")
        raise

