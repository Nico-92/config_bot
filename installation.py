def installPrograms():
	import manageUser
	# os.system('apt-get update')
	if programs['apache'] == '' or programs['apache'] == 'Y':
		import apache
	if programs['mysql'] == '' or programs['mysql'] == 'Y':
		os.system('apt-get install mysql-server php5-mysql --assume-yes')
	if programs['php'] == '' or programs['php'] == 'Y':
		os.system('php5 libapache2-mod-php5 php5-mcrypt --assume-yes')
	if programs['phpmyadmin'] == '' or programs['phpmyadmin'] == 'Y':
		import phpmyadmin
	if programs['git'] == '' or programs['git'] == 'Y':		
		os.system('apt-get install git --assume-yes')
	if programs['npm'] == '' or programs['npm'] == 'Y':
		os.system('apt-get install npm --assume-yes')
	if programs['wordpress'] == '' or programs['wordpress'] == 'Y':
		import wordpress