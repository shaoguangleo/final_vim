set paste
set expandtab
set textwidth=0
set shiftwidth=4

"显示行号
set number
set ruler
set wildmenu
set commentstring=\ #\ %s
set foldlevel=0
"Here to display the match line using under_line
set cursorline

"set a tab correspond 4 space
set tabstop=4


" 解决中文乱码
set encoding=utf-8
set fileencodings=utf-8,chinese,gbk,latin-1,gb2312,ucs-bom,cp936
if has("win32")
  set fileencoding=chinese
else
  set fileencoding=utf-8
endif

" 解决菜单乱码
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim

" 解决consle输出乱码
language messages zh_CN.utf-8

" 状态栏配置
set laststatus=2

" 打开语法高亮
syntax enable

" 开启语法检测
syntax on

" vimrc文件修改之后自动加载
autocmd! bufwritepost .vimrc source %

" 文件修改之后自动载入
set autoread

" yy直接复制到系统剪切板（For macvim）
"set clipboard=unnamed

" 高亮搜索命中的文本
set hlsearch

" 随着键入即时搜索
set incsearch

" 搜索时忽略大小写
set ignorecase

" 有一个或以上大写字母时仍大小写敏感
set smartcase

set guifont=Menlo:h14

colorscheme Tomorrow-Night-Bright
" 使用自带配色
"colorscheme elflord
"set background=dark

" 在状态栏显示正在输入的命令
set showcmd

" 显示括号配对情况
set showmatch

" :next, :make 命令之前自动保存
set autowrite

" 允许使用鼠标
set mouse=a

" 设置行号
set nu

" 退格键可用
set backspace=2

" 退格键一次删掉4个空格
set smarttab

" 缩进
set autoindent
set smartindent