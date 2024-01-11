#!/bin/env python3

##
## This whole script is pretty hacky for now, be warned
##

import sys
import os

config = sys.argv[1]
out_folder = sys.argv[2]

f = open(config, "r")
config_lines = f.readlines()
f.close()

for line in config_lines:
    line_split = line.split("=")
    os.chdir(out_folder)
    if (line[0] == "#"):
        #line_split = line.split(" ")
        #f = open(line_split[1], "w")
        #f.write("# " + line_split[1] + " is not set\n\n")
        print(line)
    elif (line_split[1] == "n\n"):
        f = open(line_split[0], "w")
        f.write("# " + line_split[0] + " is not set\n\n")
    else:
        f = open(line_split[0], "w")
        f.write(line + "\n")
    f.close()
