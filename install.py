#!/usr/bin/env python

'''
The script will install the final-vim automatically
'''

import subprocess
import os
import time


# Default setting
final_vim_path = os.environ['HOME'] + '/' + '.final_vim'
bundle_path = os.path.join(final_vim_path + '/bundle')

def welcome():
    'Here will download the whole final-vim git repo'
    print 'Welcome my friend!'
    stay_sec = 3
    print 'You are about to install final_vim. Ready? Let us do the awesome thing in %d seconds.' % stay_sec
    time.sleep(stay_sec)
    print '*'*60
    print 'Now begin to install the final_vim'
    print '*'*60

def show_info():
    'Will show information when finish install final_vim'
    print 'There you are.'
    print 'Welcome to the final_vim world'
    print 'Any issue/need/question, goto https://github.com/shaoguangleo/final_vim, see you there.'
    print 'Anyway, Enjoy!!!'

def install_plugins():
    'Will install all the bundle plugins'
    #cmd = 'vim +PluginInstall +qall 2>/dev/null'
    cmd = 'vim +PluginInstall +qall '
    res = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
    stdoutput = res.communicate()

def link_vimrc():
    'Will link default vimrc to final_vim'
    cmd = 'ln -s ' + final_vim_path +'/vimrc ' + os.environ['HOME']+'/.vimrc'
    res = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    stdoutput = res.communicate()
    print 'Had link the final_vimrc to .vimrc'

welcome()

if os.path.exists(final_vim_path):
    print 'Final_vim directory had been created'
else:
    res = subprocess.Popen('mkdir ' + final_vim_path, shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = res.communicate()

if os.path.exists(bundle_path):
    print 'Bundle directory had been created'
else:
    res = subprocess.Popen('mkdir ' + bundle_path, shell=True, stdout=subprocess.PIPE)
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
    res = subprocess.Popen('git clone https://github.com/shaoguangleo/final_vim.git ~/.vim', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdoutput,erroutput) = res.communicate()
else:
    os.chdir(final_vim_path)
    print os.getcwd()
    res = subprocess.Popen('git pull', shell=True, stdout=subprocess.PIPE)
    (stdoutput,erroutput) = res.communicate()

install_plugins()
link_vimrc()

print '*'*60
if empty:
    print 'Finished install the final_vim'
else:
    print 'Finished upgrade the final_vim'
print '*'*60

show_info()
