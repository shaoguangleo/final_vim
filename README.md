# final_vim
配置最终vim环境的简便方法
The easiest way to config the VIM - final vim

# 一步搞定
下载**install.py** ,运行**./install.py**即可将**final_vim**安装到你的系统中，下面可以一个命令搞定

```
curl -L https://raw.github.com/shaoguangleo/final_vim/master/install.py | python
```

# 如何安装
##配置安装VundleVim

在安装VundleVim之前需要先行安装**git和curl**。

1.首先下载

```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```
2.放置一个模板在.vimrc的最上方。

```
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Avoid a name conflict with L9
Plugin 'user/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line
```

##安装插件
 - 打开vim，然后运行**:PluginInstall**即可。
 - 命令行安装**$ vim + PluginInstall + qall**

##插件列表
- [nerdtree](https://github.com/scrooloose/nerdtree) A tree explorer plugin for vim.
- [nerdcommenter](https://github.com/scrooloose/nerdcommenter) Vim plugin for intensely orgasmic commenting
- [tagbar](https://github.com/majutsushi/tagbar) Vim plugin that displays tags in a window(ctags is needed)
- [ctrlp](https://github.com/kien/ctrlp.vim) Fuzzy file, buffer, mru, tag, etc finder.
- [vim-airline](https://github.com/bling/vim-airline) lean & mean status/tabline for vim that's light as air
- [vim-snippets](https://github.com/honza/vim-snippets) vim-snipmate default snippets
- [UltiSnips](https://github.com/SirVer/ultisnips) The ultimate snippet solution for Vim
- [vim-surround](https://github.com/tpope/vim-surround) quoting/parenthesizing made simple
- [vim-instant-markdown](https://github.com/suan/vim-instant-markdown) Instant Markdown previews from VIM!
- [vim-multiple-cursors](https://github.com/terryma/vim-multiple-cursors) True Sublime Text style multiple selections for Vim
- [vim-startify](https://github.com/mhinz/vim-startify) A fancy start screen for Vim
- [vim-emoji](https://github.com/junegunn/vim-emoji) Named Emoji in Vim
- [vim-json-line-format](https://github.com/axiaoxin/vim-json-line-format) format json line
- [jedi-vim](https://github.com/davidhalter/jedi-vim) Using the jedi autocompletion library for VIM.
- [vim-flake8](https://github.com/nvie/vim-flake8) Flake8 plugin for Vim
- [indentLine](https://github.com/Yggdroot/indentLine) A vim plugin to display the indention levels with thin vertical lines
- [vim-gitgutter](https://github.com/airblade/vim-gitgutter) A Vim plugin which shows a git diff in the gutter (sign column) and stages/reverts hunks.
- [favorite-vim-colorscheme](https://github.com/axiaoxin/favorite-vim-colorscheme) Tomorrow night bright color scheme
- [vim-node](https://github.com/moll/vim-node) Tools and environment to make Vim superb for developing with Node.js. Like Rails.vim for Node.
- [jshint](https://github.com/jshint/jshint) JSHint is a tool that helps to detect errors and potential problems in your JavaScript code
- [vim-javascript-syntax](https://github.com/jelera/vim-javascript-syntax) Enhanced javascript syntax file for Vim
- [vim-coloresque](https://github.com/gorodinskiy/vim-coloresque) css/less/sass/html color preview for vim
- [vim-table-mode](https://github.com/dhruvasagar/vim-table-mode) VIM Table Mode for instant table creation.
- [emmet-vim](https://github.com/mattn/emmet-vim) emmet for vim: <http://mattn.github.io/emmet-vim>


# how to upgrade

# OS

### 安装依赖

首先肯定需要**git vim ctags**

## MacOSX

### VIM版本
 - Vim - Vi IMproved 7.4 (2013 Aug 10)
 - MacOSX - EI Capitan 10.11.3

### 安装依赖
```
brew install vim git npm ctags
sudo npm -g install instant-markdown-d jshint
sudo pip install isort jedi yapf flake8 virtualenvwrapper
```
