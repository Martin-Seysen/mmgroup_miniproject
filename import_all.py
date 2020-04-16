import sys 
import os
import time
sys.path.insert(0, os.path.abspath("src"))
#print(sys.path)

print("Importing python dlls..")
t_start = time.time()
import miniproject 
from miniproject import mini_double
from miniproject import mini_triple
t = time.time() - t_start
print("done after %.2f seconds." % t)

