syntax on

"""""""""""""""""YouCompleteMe

let g:DoxygenToolkit_authorName="Shaoguang Guo <sgguo@shao.ac.cn>"
let g:ycm_global_ycm_extra_conf='~/.final_vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
"let g:ycm_confirm_extra_conf=0


set completeopt=longest,menu

let g:ycm_key_list_previous_completion=['<Down>']
let g:ycm_key_list_previous_completion=['<Up>']
let g:ycm_collect_identifiers_from_tags_files=1
let g:ycm_min_num_of_chars_for_completion=2
let g:ycm_seed_identifiers_with_syntax=1


let g:ycm_complete_in_comments=1
let g:ycm_complete_in_strings=1
let g:ycm_collect_identifiers_from_comments_and_strings=0

"""""""""""syntastic""""""""""""""""""""
"let g:syntastic_mode_map = {'mode':'active','active_filetypes':[],'passive_filetypes':[]}
let g:syntastic_check_on_open=1
let g:syntastic_cpp_include_dirs=['/usr/include']
let g:syntastic_cpp_remove_include_errors=1
let g:syntastic_cpp_check_header=1
let g:syntastic_cpp_compiler='clang++'
let g:syntastic_cpp_compiler_options='-std=c++11 -Wall -stdlib=libc++ -Wextra -Wpendantic'
let g:syntastic_error_symbol='>>'
let g:syntastic_warning_symbol='!'
let g:syntastic_enable_balloons=1
let g:syntastic_enable_highlighting=1
let g:syntastic_enable_signs=1
let g:syntastic_python_python_exec='/bin/python2'


let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0


let NERDTreeWinPos = 'left'


""""""""""""ctags and Taglist""""""""""""""""""
let Tlist_WinWidth=34
let Tlist_Auto_Open=0
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
let Tlist_Use_SingleClick=1
"let Tlist_Use_Right_Window=1
let Tlist_File_Fold_Auto_Close=1
let Tlist_Auto_Update=1


"" make tags file
" cd $project
" ctags -R *


""" single file generate tags, Press F12
"set tags=/home/codingeveryday/pra_programming/unix_apue_src/chapter5_standard_io/tags;
set autochdir


function!UpdateTagsFile()
silent!ctags -R --c++-kinds=+p --fields=+ianS --extra=+q
endfunction
nmap <F12> :call UpdateTagsFile()<CR>


"nmap <F5> :WMToggle<CR>
nmap <F6> :Tlist<CR>
nmap <F4> zA
nmap <F3> zR
nmap <F7> :A<CR>
nmap <F8> :NERDTreeToggle<CR>
