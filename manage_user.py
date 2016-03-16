print ' =========================================\n User info \n ========================================='
rootDirectory = raw_input('Root directory:\n')
nome = raw_input('New linux user: \n')
password = raw_input('Password: \n')
dominio = raw_input('Domain of site: \n')
#Add user
os.system('useradd ' + nome )
os.system('passwd ' + password)
os.chdir('/' + rootDirectory )
# Create user directory
os.system('mkdir ' + nome)
# Create directory for website
os.chdir(nome)
os.system('mkdir htdocs')
os.chdir('htdocs')
os.system('mkdir web')
os.chdir('/' + rootDirectory + '/' + nome)
# Create directory for logs
os.system('mkdir log')
# Set correct user to directories
os.chdir('/' + rootDirectory + '/' + nome)
os.system('chown -R ' + nome + ':' + nome + ' ' + nome + '/')

