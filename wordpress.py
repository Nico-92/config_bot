import os
os.chdir('~ ')
os.system('apt-get install wget --assume-yes')
os.system('wget http://wordpress.org/latest.tar.gz')
os.system('tar xzvf latest.tar.gz')
os.system('apt-get install php5-gd libssh2-php --assume-yes')