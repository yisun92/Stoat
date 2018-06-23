import sys
import os
import subprocess
from os import listdir
from os.path import isfile, join

print "[merge_coverage.py] Start merging execution files"
script_path = os.path.dirname(os.path.realpath(__file__))
jacoco_cli_jar = join(script_path, "jacoco.cli.jar")
cov_dir = sys.argv[1]
target_file = sys.argv[2]

files = [join(cov_dir, f) for f in listdir(cov_dir) if isfile(join(cov_dir, f))]
file_str = ' '.join(files)

cmd = "java -jar %s merge %s --destfile %s" % (jacoco_cli_jar, file_str, target_file)
print cmd

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out,err = p.communicate()