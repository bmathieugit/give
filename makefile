# Crée et active l'environnement virtuel
give-venv:
	python3 -m venv give-venv
	@echo "Environnement virtuel créé. Pour l'activer, utilisez 'source give-venv/bin/activate'."

# Installe les dépendances à partir du fichier python.txt dans l'environnement virtuel
install-deps:
	give-venv/bin/pip install -r python.txt
	@echo "Dépendances installées."

# Cible par défaut pour initialiser l'environnement virtuel et installer les dépendances
init: give-venv install-deps

install: init
	. give-venv/bin/activate
	cp -f give.py give-venv/bin/give.py
	cp -f give give-venv/bin/give
	chmod +x give-venv/bin/give*
