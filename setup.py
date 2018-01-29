from setuptools import setup, find_packages

setup(
    name='final_vim',
    version='0.1',
    keywords=('final', 'vim'),
    description='final vim',
    long_description='The easiest way to config the VIM - final vim',
    license='none',
    url='https://github.com/shaoguangleo/final_vim',
    author='Shaoguang Guo',
    author_email='sgguo@shao.ac.cn',

    packages=find_packages(),
    platforms='any',
    install_requires=[],

    scripts=['install.py'],
    entry_points = {
        'console_scripts':[
            'final_vim = install:main'
        ]
    }
)
