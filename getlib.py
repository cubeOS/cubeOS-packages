#!/usr/bin/python

import sys, os, glob

libraries = ""
args = sys.argv[1:] #remove the first element from the list
if len(args) == 0:
  print "No arguments."
  exit(1)

for arg in args:
	libraries += "; LIBRARY: " + arg + " ;\n"
	
	wd = os.path.join(os.path.dirname(os.path.realpath(__file__)), arg)
	for f in glob.glob(os.path.join(wd, "*.package")):
		libraries += open(f, 'r').read() + "\n"

	libraries += "\n"

print libraries
