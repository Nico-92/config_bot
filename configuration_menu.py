print ' =========================================\n Installation \n ========================================='
choice = ''
#At the end of each choice the menu is shown again
while choice != '0':
	choice = raw_input(' 1 - Install everything \n 2 - Select what to install\n 3 - Install custom program \n 4 - Show all programs\n 0 - Exit\n')
	if choice == '1':
		# Set to true all programs, this meansall programs will be installed
		for key, value in programs.iteritems():
			programs[key] = 'Y'
			installPrograms()
	elif choice == '2':
		# Ask to the user if he wants to install a program
		for key, value in programs.iteritems():
			programs[key] = raw_input( 'Vuoi installare ' + key + '? (Y,n)\n')
		installPrograms()
	elif choice == '3':
		# ask to the user the name of the program he wants to install
		custom = raw_input('Nome pacchetto\n')
	elif choice == '4':
		# Print all programs
		for key, value in programs.iteritems():
			print key