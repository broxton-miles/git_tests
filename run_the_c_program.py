import sys
import subprocess as sp
try:
	sp.check_call(["g++","howdy.cpp"])
except:
	print("There was a problem compiling the program")
if (sp.check_output(["./a.out"]).rstrip() != "Howdy"):
	print("The code compiled, but expected output was not returned")
else:
	print("Everything is good")
