#!/usr/bin/env python3
# Moving and Renaming Files and Folders

# Imports
import shutil
import os

# Start from usr dir
os.chdir('/home/student/mycode/')

# Move of file or folder from source path to destination path
shutil.move('raynor.obj', 'ceph_storage/')

# If it already exists, do not overwrite but ask usr for new name
xname = input('What is the new name for kerrigan.obj? ')

# Execute the new name provided by usr
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


