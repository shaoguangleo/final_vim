#!/usr/bin/env python

'''
The script will install the final-vim automatically
'''

import subprocess
import os

'Here will download the whole final-vim git repo'
print '*'*60
print 'Now begin to install the final_vim'
print '*'*60

final_vim_path = os.environ['HOME'] + '/' + '.final_vim'

if os.path.exists(final_vim_path):
    print 'Directory had been created'
else:
    res = subprocess.Popen('mkdir ' + final_vim_path, shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = res.communicate()

empty = True
#for root, dirs, files in os.walk(final_vim_path):
#    if(len(files) == 0):
#        empty = True
#    else:
#        empty = False
temp = os.listdir(final_vim_path)

empty = (temp == [])

print empty

if empty:
    res = subprocess.Popen('git clone https://github.com/shaoguangleo/final_vim.git ~/.final_vim', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdoutput,erroutput) = res.communicate()
else:
    os.chdir(final_vim_path)
    print os.getcwd()
    res = subprocess.Popen('git pull', shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = res.communicate()

print '*'*60
if empty:
    print 'Finished install the final_vim'
else:
    print 'Finished upgrade the final_vim'
print 'Enjoy!!!'
print '*'*60
