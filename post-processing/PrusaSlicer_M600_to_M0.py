#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

FILE_PATH = sys.argv[1]

FIND_GCODE = 'M600'
REPLACE_GCODE = 'M0\n'
SKIP_LINE = 'post_process'

DEBUG = False

# Open input file
file_input = open(FILE_PATH, "r")
# Open output file 
file_output = open(FILE_PATH + ".new", "w")

if DEBUG:
  print('----- Variables ---------')
  print('File: ' + FILE_PATH)
  print('Find GCODE: "' + FIND_GCODE + '"')
  print('Replace GCODE: "' + REPLACE_GCODE + '"')
  print('-------------------------')
  print('')
  
# Modify file
for line in file_input:
  if DEBUG:
    print('Line: ' + line)
  if FIND_GCODE in line and SKIP_LINE not in line:
    if DEBUG: 
      print('############################')
      print('Match found in line: ' + line)
      print('############################')
    if DEBUG:
      print('Replaced line: ' + REPLACE_GCODE)
      print('-------------------------------------')
    file_output.write(REPLACE_GCODE)
  else:
    file_output.write(line)
    
 # Close files
file_input.close()
file_output.close()

# Replace files
os.remove(FILE_PATH)
os.rename(FILE_PATH + ".new", FILE_PATH)