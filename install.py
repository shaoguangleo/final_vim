#!/usr/bin/env python
###############################################################################
#
# Copyright (C) 2016-2018
# Division of Radio Astronomy Science and Technology
# SHAO (Shanghai Astronomical Observatory) <http://www.shao.ac.cn>
# CAS (Chinese Academy of Sciences)
# Postal adress: No. 80 Nandan Road , Xuhui District,
#                Shanghai, 200030 P. R. China

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

#-------------------------------------------------------------------------------
# Name:         install.py
# Purpose:      Install final_vim automatically in one step
#
# Author:       Shaoguang Guo (SHAO)
# Phone:        +86-21-34775565
#
# Created:      29-11-2016
#-------------------------------------------------------------------------------


import os
import time
import time as t

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
home_path = os.environ['HOME']
stay_sec = 2

def print_msg(msg):
    print ('')
    print ('*'*60)
    print ('>>> ' + msg)
    print ('*'*60)


def welcome():
    'Here will download the whole final-vim git repo'
    print ('Welcome my friend!')
    print ('You are about to install final_vim. Ready? Let us do the awesome thing in %d seconds.') % stay_sec
    time.sleep(stay_sec)
    print_msg('Now begin to install the final_vim')

def show_info():
    'Will show information when finish install final_vim'
    print ('There you are.')
    print ('Welcome to the final_vim world')
    print ('Any issue/need/question, goto https://github.com/shaoguangleo/final_vim, see you there.')
    print ('Anyway, Enjoy!!!')
    print (name)


def install_dependency():
    print_msg('Now install dependecy software')
    time.sleep(stay_sec)
    if not os.path.exists(final_vim_path + '/bundle/Vundle.vim'):
        os.system('git clone https://github.com/VundleVim/Vundle.vim.git ' + final_vim_path + '/bundle/Vundle.vim')
    else:
        os.system('cd ' + final_vim_path + '/bundle/Vundle.vim')
        os.system('git pull')

    if not os.path.exists(final_vim_path + '/vim-plugins/README.md'):
        os.system('git clone  https://github.com/WolfgangMehner/vim-plugins ' + final_vim_path + '/vim-plugins')
    else:
        os.system('cd ' + final_vim_path + '/vim-plugins')
        os.system('git pull')
    print ('Update the Template')
    os.system('cp Templates ' + final_vim_path + '/vim-plugins/template-support/templates/')

    if os.path.exists('/etc/debian_version'):
        os.system('sudo apt-get install -y python-flake8 python3-flake8 flake flake8 exuberant-ctags')
    elif os.path.exists('/etc/redhat_version'):
        os.system('sudo yum install -y python-flake8 ctags')

def install_plugins():
    print ('Will install all the bundle plugins')
    cmd = 'vim +PluginInstall +qall 2>/dev/null'
    os.system(cmd)

def link_vimrc():
    'Will link default vimrc to final_vim'
    cmd = 'ln -fFs ' + final_vim_path +'/vimrc ' + os.environ['HOME']+'/.vimrc'
    os.system(cmd)
    print ('Had link the final_vimrc to .vimrc')

def final_vim_done():
    print_msg('Finished install/upgrade the final_vim')


def install_final_vim():
    if not os.path.exists(final_vim_path):
        print_msg ('Now will clone the repo')
        cmd = 'git clone https://github.com/shaoguangleo/final_vim.git ~/.final_vim/'
        os.system(cmd)
    else:
        print_msg ('Now will update the repo')
        os.system('cd ' + final_vim_path)
        os.system('git pull')

def get_now_time():
    now = t.time()
    gmt = t.gmtime(now)
    return (t.strftime('%Y-%m-%d-%H-%M-%s', gmt))

def back_up_vim():
    nowtime = get_now_time()
    if os.path.exists(home_path + "/.vim"):
        print_msg ('Now back up vim => ~/.vim_' + nowtime)
        cmd = 'mv ' + home_path + '/.vim ' + home_path + '/.vim_'+nowtime
        os.system(cmd)
    if os.path.isfile(home_path + "/.vimrc"):
        print_msg ('Now back up vim => ~/.vimrc_' + nowtime)
        cmd = 'mv ' + home_path + '/.vimrc ' + home_path + '/.vimrc_'+nowtime
        os.system(cmd)
    print_msg("Finish Backup")


if __name__ == '__main__':
    welcome()
    back_up_vim()
    install_final_vim()
    install_dependency()
    install_plugins()
    link_vimrc()
    final_vim_done()
    show_info()
