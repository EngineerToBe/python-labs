import re
import sys

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
 <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
 <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
  """
  names = []
  new_dict = {}
  #file = open(filename, 'r')
  #text = file.read()

  with open(filename, 'r') as f:
      text = f.read()
  year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
  if not year_match:
      sys.stderr.write("Not string found")
      sys.exit(1)
  #year = year_match
  names.append(year_match)
  #print(names)

  names_match = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
  #print(names_match)
  for rank in names_match:
      (rank, boyname, girlname) = rank
      if boyname not in new_dict:
          new_dict[boyname] = rank
      if girlname not in new_dict:
          new_dict[girlname] = rank
  sorted_names = sorted(new_dict.keys())
  for name in sorted_names:
    names.append(name + " " + new_dict[name])
  return names




print(extract_names("/home/aaa/Code/Python/codeacademy/google_python/baby1990.html"))
