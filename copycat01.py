#!/usr/bin/env python3
# Copying files and folders 

# Import statements and modules
import shutil
import os

# Start from home usr dir
os.chdir("/home/student/mycode/")

# cp file to folder
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# cp folder and files contained
shutil.copytree("5g_research/", "5g_research_backup/")

