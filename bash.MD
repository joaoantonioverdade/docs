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

## Folder structure

* ```~```, user home
* ```.``` or ```pwd```, current
* ```..```, parent
* ```-```, last

## References

[Bashism](http://mywiki.wooledge.org/Bashism)
