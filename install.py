#!/usr/bin/env python

'''
The script will install the final-vim automatically
'''

import subprocess
import os
import time

name = '''
 _____ ___ _   _    _    _       __     _____ __  __
|  ___|_ _| \ | |  / \  | |      \ \   / /_ _|  \/  |
| |_   | ||  \| | / _ \ | |   ____\ \ / / | || |\/| |
|  _|  | || |\  |/ ___ \| |__|_____\ V /  | || |  | |
|_|   |___|_| \_/_/   \_\_____|     \_/  |___|_|  |_|

'''

# Default setting
final_vim_path = os.environ['HOME'] + '/' + '.final_vim'
bundle_path = os.path.join(final_vim_path + '/bundle')
stay_sec = 2

def welcome():
    'Here will download the whole final-vim git repo'
    print 'Welcome my friend!'
    print 'You are about to install final_vim. Ready? Let us do the awesome thing in %d seconds.' % stay_sec
    time.sleep(stay_sec)
    print ('')
    print ('*'*60)
    print ('Now begin to install the final_vim')
    print ('*'*60)

def show_info():
    'Will show information when finish install final_vim'
    print 'There you are.'
    print 'Welcome to the final_vim world'
    print 'Any issue/need/question, goto https://github.com/shaoguangleo/final_vim, see you there.'
    print 'Anyway, Enjoy!!!'
    print (name)


def install_dependency():
    'Will install all the dependency software'
    print ('')
    print ('*'*60)
    print('Now install dependecy software')
    print ('*'*60)
    time.sleep(stay_sec)
    if not os.path.exists('~/.vim/bundle/Vundle.vim'):
        os.system('git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim')
    else:
        os.system('cd ~/.vim/bundle/Vundle.vim')
        os.system('git pull')

    if os.path.exists('/etc/debian_version'):
        os.system('apt-get install -y python-flake8 python3-flake8 flake flake8')
    elif os.path.exists('/etc/redhat_version'):
        os.system('yum install -y python-flake8')

def install_plugins():
    print ('Will install all the bundle plugins')
    cmd = 'vim +PluginInstall +qall 2>/dev/null'
    os.system(cmd)

def link_vimrc():
    'Will link default vimrc to final_vim'
    cmd = 'ln -fFs ' + final_vim_path +'/vimrc ' + os.environ['HOME']+'/.vimrc'
    os.system(cmd)
    print 'Had link the final_vimrc to .vimrc'

def final_vim_done():
    print '*'*60
    print 'Finished install/upgrade the final_vim'
    print '*'*60


def install_final_vim():
    if not os.path.exists(final_vim_path):
        print ('Now will clone the repo')
        cmd = 'git clone https://github.com/shaoguangleo/final_vim.git ~/.final_vim/' 
        os.system(cmd)
    else:
        print ('Now will update the repo')
        os.system('cd ' + final_vim_path)
        os.system('git pull')

welcome()
install_dependency()
install_final_vim()
install_plugins()
link_vimrc()
final_vim_done()
show_info()
