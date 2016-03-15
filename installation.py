def installPrograms():
	# os.system('apt-get update')
	if programs['apache'] == '' or programs['apache'] == 'Y':
		os.system('apt-get install apache2 --assume-yes')	
	if programs['mysql'] == '' or programs['mysql'] == 'Y':
		os.system('apt-get install mysql-server php5-mysql --assume-yes')
	if programs['php'] == '' or programs['php'] == 'Y':
		os.system('php5 libapache2-mod-php5 php5-mcrypt --assume-yes')
	if programs['phpmyadmin'] == '' or programs['phpmyadmin'] == 'Y':
		os.system('apt-get install phpmyadmin apache2-utils --assume-yes')
	if programs['phpmyadmin'] == '' or programs['phpmyadmin'] == 'Y':
		os.system('apt-get install git apache2-utils --assume-yes')