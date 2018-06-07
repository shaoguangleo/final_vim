" Name  : vimrc  : for final_vim
" Author: Guo Shaoguang <shaoguangleo@163.com>
" Source: https://github.com/shaoguangleo/final_vim
"
"
" Enjoy.
"

" Here for Vundle vim
" source ~/.vim/bundle.vim

source ~/.final_vim/vimrc_general.vim

" Import the plugins
source ~/.final_vim/plugins.vim
source ~/.final_vim/plugins_setting.vim

" Here for pythoner
" source ~/.final_vim/python.vim

" Adding the title when create a new file
source ~/.final_vim/new_title.vim

" Setting the color schme
set runtimepath+=~/.final_vim
set runtimepath+=~/.final_vim/vim-plugins
set runtimepath+=~/.final_vim/bundle
colorscheme Tomorrow-Night-Bright
