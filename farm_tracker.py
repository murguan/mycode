#!/usr/bin/env python3
import time
import os
from subprocess import call
import yaml
import crayons
import requests

FARMSURL = "https://labs.alta3.com/demo/farms.yaml"

def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

def farmcount(farms):
  i = 0
  for farm in farms:
      i += 1
  return i

def farmstatus():
    farmsresp = requests.get(FARMSURL)
    farmlife = farmsresp.text
    farms = yaml.safe_load(farmlife)
    clear()
    #print title in bold green
    print(crayons.green(f"Old Mac has {farmcount(farms)} farms, they are:", bold=True))
    # farm will be equal to one of the dict within the list "farms"
    for farm in farms:
        #print name of the farms in bold yellow
        print(crayons.yellow(f"{farm.get('name')}, which is raising: ", bold=True))
        # from a single "farm" get the list from the key "agriculture"
        for agri in farm.get('agriculture'):
            #print agriculture in bold blue
            print(crayons.blue(f" - {agri}", bold=True))
    print(crayons.green("Ctrl-c to quit"))

def main():
    try:
        while True:
            farmstatus()
            time.sleep(20)
    except KeyboardInterrupt:
        pass


main()

