# Bash

At startup reads and executes commands from:

* /etc/profile

After that, reads and executes commands from the first one that exists from:

* ~/.bash_profile
* ~/.bash_login
* ~/.profile

When the shell exits, Bash reads and executes:

* ~/.bash_logout

When an interactive shell that is not a login shell is started:

* ~/.bashrc

#### Folder structure

* ```~```, user home
* ```.``` or ```pwd```, current
* ```..```, parent
* ```-```, last

#### Piping

\# Run command2 if command1 succeeds

`command1 && command2`

\# Run command2 if command1 fails

`command1 || command2`

\# Run both commands

`command1 ; command2`


#### Command line miscellaneous

\# Alias for last command arguments

`command !*`

\# Background running

`nohup command.sh > log.out 2> log.err < /dev/null &`

\# Symbolic link

`ln -s target source`

\# Compress and decompress

tar -zcvf result.tar.gz folder/

tar -zxvf compressed.tar.gz

### Text operations

\# To know by heart: head, tail, cat, wc, diff, sdiff, sort, uniq, **cut**, **paste**, grep, tree, jobs

\# lowercase file

cat input | tr '[:upper:]' '[:lower:]' > output

\# range of lines from file
sed -n 10,100p input

#### Search

\# Search filename

`find . -name '*.ext'`

#### SSH

\# Copying from SSH to local:

`scp user@0.0.0.0:filename /local/file`

`scp -r user@0.0.0.0:folder/ /local/dir`

\# Copying from local to SSH:

`scp /home/file user@0.0.0.0:/remote/file`



#### Shortcuts

Shortcuts     | Action
--------------|------------------------------------
CTRL + A      | start of the command line
CTRL + C      | kills current process
CTRL + D      | logout
CTRL + E      | end of the command line
CTRL + R/S    | reverse-i-search
CTRL + U      | erases all to the left of cursor
CTRL + K      | erases all to the right of cursor
CTRL + W      | erases token by token
CTRL + Z      | stops process


## Environment variables

Variable      | Contains
--------------|------------------------
HOME          | home directory
TERM          | terminal type
SHELL         | path to shell
USER          | login name
PATH          | a list to search for programs


## Programming


## Encoding

Find encoding

'file -bi filename' 

Convert from encoding

iconv -f iso-xpto -t utf-8 input.txt > output.txt


### References

[Reference Manual](http://www.gnu.org/software/bash/manual/bash.pdf)

[Tools Summary](http://www.tldp.org/LDP/GNU-Linux-Tools-Summary/GNU-Linux-Tools-Summary.pdf)

[Bash Beginners Guide](http://www.tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf)

[Advanced Bash-Scripting Guide](http://www.tldp.org/LDP/abs/html/)

[Bash Programming Introduction HOW-TO](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
