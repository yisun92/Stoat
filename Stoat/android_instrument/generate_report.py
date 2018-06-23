import subprocess
import sys


cmd = ' '.join(sys.argv[1:])
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = p.communicate()
print out
print err