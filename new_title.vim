"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""新文件标题
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"新建.c,.h,.sh,.java文件，自动插入文件头 
autocmd BufNewFile *.cpp,*.[ch],*.sh,*.rb,*.java,*.py exec ":call SetTitle()" 
""定义函数SetTitle，自动插入文件头 
func SetTitle() 
	"如果文件类型为.sh文件 
    if expand("%:e") == 'sh' 
		call setline(1,"\#!/bin/bash") 
		call append(line("."), "") 
    elseif expand("%:e") == 'py' "For python 
        call setline(1,"#!/usr/bin/env python")
        call append(line("."),"# coding=utf-8")
	    call append(line(".")+1, "#")
        call append(line(".")+2, "###############################################################################")
        call append(line(".")+3, "# Copyright (C) 2010 - ".strftime("%Y"))
        call append(line(".")+4, "# Division of Radio Astronomy Science and Technology")
        call append(line(".")+5, "# SHAO (Shanghai Astronomical Observatory) <http://www.shao.ac.cn>")
        call append(line(".")+6, "# CAS (Chinese Academy of Sciences)")
        call append(line(".")+7, "# Postal adress: 80# Nandan Road , Xuhui District, Shanghai, 200030 P. R. China")
        call append(line(".")+8, "###############################################################################")
        call append(line(".")+9, "#")
        call append(line(".")+10, "#-------------------------------------------------------------------------------")
        call append(line(".")+11, "# File Name   :   ".expand("%"))
        call append(line(".")+12, "# Purpose     :   ")
        call append(line(".")+13, "#")
        call append(line(".")+14, "# Author      :   Shaoguang Guo (SHAO)")
        call append(line(".")+15, "# Email       :   sgguo@shao.ac.cn")
        call append(line(".")+16, "# Created     :   ".strftime("%Y-%m-%d %H:%M:%S"))
        call append(line(".")+17, "# Modified    :   ".strftime("%Y-%m-%d %H:%M:%S"))
        call append(line(".")+18, "#-------------------------------------------------------------------------------")
        call append(line(".")+19, "#")

    elseif expand("%:e") == 'rb' "For ruby
        call setline(1,"#!/usr/bin/env ruby")
        call append(line("."),"# encoding: utf-8")
	    call append(line(".")+1, "#")
        call append(line(".")+2, "###############################################################################")
        call append(line(".")+3, "# Copyright (C) 2010 - ".strftime("%Y"))
        call append(line(".")+4, "# Division of Radio Astronomy Science and Technology")
        call append(line(".")+5, "# SHAO (Shanghai Astronomical Observatory) <http://www.shao.ac.cn>")
        call append(line(".")+6, "# CAS (Chinese Academy of Sciences)")
        call append(line(".")+7, "# Postal adress: 80# Nandan Road , Xuhui District, Shanghai, 200030 P. R. China")
        call append(line(".")+8, "###############################################################################")
        call append(line(".")+9, "#")
        call append(line(".")+10, "#-------------------------------------------------------------------------------")
        call append(line(".")+11, "# File Name   :   ".expand("%"))
        call append(line(".")+12, "# Purpose     :   ")
        call append(line(".")+13, "#")
        call append(line(".")+14, "# Author      :   Shaoguang Guo (SHAO)")
        call append(line(".")+15, "# Email       :   sgguo@shao.ac.cn")
        call append(line(".")+16, "# Created     :   ".strftime("%Y-%m-%d %H:%M:%S"))
        call append(line(".")+17, "# Modified    :   ".strftime("%Y-%m-%d %H:%M:%S"))
        call append(line(".")+18, "#-------------------------------------------------------------------------------")
        call append(line(".")+19, "#")

"    elseif &filetype == 'mkd'
"        call setline(1,"<head><meta charset=\"UTF-8\"></head>")
	else 
		call setline(1, "/**") 
        call append(line(".")   , "* Copyright (C) 2010 - ".strftime("%Y"))
        call append(line(".") +1, "* Division of Radio Astronomy Science and Technology")
        call append(line(".")+2, "* SHAO (Shanghai Astronomical Observatory) <http://www.shao.ac.cn>")
        call append(line(".")+3, "* CAS (Chinese Academy of Sciences)")
        call append(line(".")+4, "* Postal adress: 80# Nandan Road , Xuhui District, Shanghai, 200030 P. R. China")
        call append(line(".")+5, "*")
		call append(line(".")+6, "* @file           :   ".expand("%")) 
		call append(line(".")+7, "* @author         :   Guo Shaoguang ") 
        call append(line(".")+8, "* @mail           :   sgguo@shao.ac.cn") 
        call append(line(".")+9, "* @version        :   v1.0") 
        call append(line(".")+10,"* @created        :   ".strftime("%Y-%m-%d %H:%M:%S"))
        call append(line(".")+11,"* @modified       :   ".strftime("%Y-%m-%d %H:%M:%S"))
		call append(line(".")+12, "*/") 
		call append(line(".")+13, "")
	endif
	if expand("%:e") == 'cpp'
		call append(line(".")+14, "#include<iostream>")
		call append(line(".")+15, "using namespace std;")
		call append(line(".")+16, "")
	endif
	if expand("%.e") == 'c'
		call append(line(".")+14, "#include<stdio.h>")
		call append(line(".")+15, "")
	endif
	if expand("%:e") == 'h'
		call append(line(".")+14, "#ifndef _".toupper(expand("%:r"))."_H")
		call append(line(".")+15, "#define _".toupper(expand("%:r"))."_H")
		call append(line(".")+16, "#endif")
	endif
	if expand("%.e") == 'java'
		call append(line(".")+14,"public class ".expand("%:r"))
		call append(line(".")+15,"")
	endif
	"新建文件后，自动定位到文件末尾
endfunc 
autocmd BufNewFile * normal G

func DateInsert()
    call cursor(9,1)
    if search('Modified') != 0
        let line = line('.')
        call setline(line, '# Modified    :   '.strftime("%Y-%m-%d %H:%M:%S"))
    endif
    if search('modified') != 0
        let line = line('.')
        call setline(line, '* @modified       :   '.strftime("%Y-%m-%d %H:%M:%S"))
    endif
endfunc

autocmd FileWritePre,BufWritePre *.cpp,*.[ch],*.sh,*.rb,*.java,*.py ks|call DateInsert() | 's 
