# Crée et active l'environnement virtuel
give-venv:
	python3 -m venv give-venv
	@echo "Environnement virtuel créé. Pour l'activer, utilisez 'source give-venv/bin/activate'."

# Installe les dépendances à partir du fichier python.txt dans l'environnement virtuel
install:
	give-venv/bin/pip install -r python.txt
	@echo "Dépendances installées."

# Cible par défaut pour initialiser l'environnement virtuel et installer les dépendances
init: give-venv install

