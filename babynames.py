#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  #initialise vars
  ret_list = []
  name_dict = {}

  #open file and read contents
  file_obj = open(filename,'r')
  file_contents = file_obj.read()

  #extract data with tags from html file
  year_string = re.search(r'popularity in \d+', file_contents, re.IGNORECASE)
  name_and_rank_list = re.findall(r'(<td>.*?</td>)(<td>.*?</td>)(<td>.*?</td>)', file_contents)

  #extract year
  year = re.search(r'\d+', year_string.group())
  
  #extract headers
  #for header_elem in header_list:
  #  ret_list.append(header_elem[1])

  #extract name and rank
  for name_and_rank_tuple in name_and_rank_list:
    rank = re.sub('<.*?td>', '', name_and_rank_tuple[0])
    name_male = re.sub('<.*?td>', '', name_and_rank_tuple[1])
    name_female = re.sub('<.*?td>', '', name_and_rank_tuple[2])
    name_dict[rank] = (name_male, name_female)
    ret_list.append(name_male+' '+rank)
    ret_list.append(name_female+' '+rank)

  #adjust return list
  ret_list = sorted(ret_list)
  ret_list.insert(0, year.group())
  
  #write result to file
  write_to_file_content = '-----Printing result for the file %s-----\n%s' %(filename, ret_list)
  write_to_file = 'summary/%s.summary' %(filename)
  write_to_file_obj = open(write_to_file, 'w')
  write_to_file_obj.write(write_to_file_content)

  #Print result
  #print '-----Printing result for the file %s-----\n%s' %(filename, ret_list)
  print 'Summary printed to the file %s' %(write_to_file)

  #close file
  file_obj.close()
  write_to_file_obj.close()
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
  #create summary dir
  if not os.path.isdir('summary'):
    os.makedirs('summary')
  
  #read file contents
  for each_file in args:
    extract_names(each_file)
  
if __name__ == '__main__':
  main()
