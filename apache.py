import os
os.system('apt-get install apache2 --assume-yes')
os.system('sudo usermod www-data --append --groups ' + nome)
os.chdir('/etc/apache2/sites-available')
os.system('touch' + nome + '.conf')
virtual = '<VirtualHost *:80>ServerName ' + dominio + ' ServerAlias http://www.' + dominio
virtual += 'DocumentRoot /' + rootDirectory + '/' + nome + '/htdocs/web';
virtual += 'ErrorLog /' + rootDirectory + '/' + nome + '/logs/error.log'
virtual += 'CustomLog /' + rootDirectory + '/' + nome + '/logs/access.log combined' 
virtual += '<Directory "/' + rootDirectory + '/' + nome + '/htdocs/web">'
virtual += 'Order allow,deny Allow from all Require all granted'
virtual += 'Options FollowSymLinks AllowOverride All </Directory>'
virtual += '</VirtualHost>'
file = open(nome + '.conf', 'w')
file.write(virtual)
file.close()
os.system('a2ensite ' + nome + '.conf')
os.system('a2dissite 000-default.conf')
os.system('service apache2 restart')
