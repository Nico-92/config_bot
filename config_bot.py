import os
programs = {'apache': '', 'mysql': '', 'php': '', 'phpmyadmin': ''}
print ' =========================================\n Installazione \n ========================================='
scelta = raw_input(' 1 - Installa tutti i pacchetti\n 2 - Seleziona pacchetti da installare\n 3 - Installa pacchetto custom\n 4 - Vedi lista pacchetti\n')

def sceltadue():
	# os.system('apt-get update')
	if programs['apache'] == '' or programs['apache'] == 'Y':
		os.system('apt-get install apache2 --assume-yes')	
	if programs['mysql'] == '' or programs['mysql'] == 'Y':
		os.system('apt-get install mysql-server php5-mysql --assume-yes')
	if programs['php'] == '' or programs['php'] == 'Y':
		os.system('php5 libapache2-mod-php5 php5-mcrypt --assume-yes')
	if programs['phpmyadmin'] == '' or programs['phpmyadmin'] == 'Y':
		os.system('apt-get install phpmyadmin apache2-utils --assume-yes')

if scelta == '1':
	for key, value in programs.iteritems():
		programs[key] = 'Y'
		sceltadue()
elif scelta == '2':
	for key, value in programs.iteritems():
		programs[key] = raw_input( 'Vuoi installare ' + key + '? (Y,n)\n')
	sceltadue()
elif scelta == '3':
	custom = raw_input('Nome pacchetto\n')
elif scelta == '4':
	for key, value in programs.iteritems():
		print key
print ' =========================================\n Configurazione \n ========================================='
rootDirectory = raw_input('Root directory:\n')
nome = raw_input('Nuovo utente Linux: \n')
password = raw_input('Password utente Linux: \n')
dominio = raw_input('Nome dominio: \n')
os.system('useradd ' + nome )
os.system('passwd ' + password)
os.chdir('/' + rootDirectory )
os.system('mkdir ' + nome)
os.system('chown -R ' + nome + ':' + nome + ' ' + nome + '/')
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
