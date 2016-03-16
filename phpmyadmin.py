import os
os.system('apt-get install phpmyadmin apache2-utils --assume-yes')
os.chdir('/etc/apache2/')
file = open('apache2.conf', 'w')
file.write("Include /etc/phpmyadmin/apache.conf")
os.system('service apache2 restart')