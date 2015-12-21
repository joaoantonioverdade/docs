# Git

### Install

sudo apt-get install git

### Configuration

* git config --global user.name "joaoantonioverdade"

* git config --global user.email "joao.antonio.verdade@gmail.com"

### Creating new repo

* git init <directory>

* create through the github interface the new repository

* git remote add origin https://github.com/joaoantonioverdade/newrepository.git

### Pull from repo

* git init <directory>

* git clone git@github.com:joaoantonioverdade/newrepository.git

# References

[SSH keys] (https://help.github.com/articles/generating-ssh-keys/)


### Github independent

#### server

* git init --bare project_name.git

#### client

* git clone ssh://user@server/folder/rep.git <directory>