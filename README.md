# final_vim

配置最终vim环境的简便方法

The easiest way to config the VIM - final vim

```
 _____ ___ _   _    _    _       __     _____ __  __ 
|  ___|_ _| \ | |  / \  | |      \ \   / /_ _|  \/  |
| |_   | ||  \| | / _ \ | |   ____\ \ / / | || |\/| |
|  _|  | || |\  |/ ___ \| |__|_____\ V /  | || |  | |
|_|   |___|_| \_/_/   \_\_____|     \_/  |___|_|  |_|                                                     
```



# ONE STEP  一步搞定

下载**install.py** ,运行**./install.py**即可将**final_vim**安装到你的系统中，下面可以一个命令搞定

```
curl -L https://raw.github.com/shaoguangleo/final_vim/master/install.py | python
```

or

```
wget -L https://raw.github.com/shaoguangleo/final_vim/master/install.py | python
```


# 快捷键

命令 | 说明
----|-----
F3        | 打开目录树
F4        | 显示TagList
F5        | 运行该脚本
F6        | 新建标签页
F7        |
F8        | PEP8检测
Ctrl+w +v | 左右分割窗口
Ctrl+w +s |上下分割窗口
Ctrl+w  +q |关闭窗口

## 插件列表

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


# TODO

## MacOSX安装依赖
```
brew install vim git npm ctags
sudo npm -g install instant-markdown-d jshint
sudo pip install isort jedi yapf flake8 virtualenvwrapper
```
