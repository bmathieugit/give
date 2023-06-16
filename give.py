import os
import subprocess
import yaml
import argparse
from termcolor import colored

def download_git_repo(repo_url, target_dir, version):
    # Utilisez la commande 'git clone' pour télécharger le dépôt Git dans le répertoire cible
    print(f"[GIVE] : téléchargement de la dépendance {repo_url}:{version} dans le répertoire {target_dir}\n")
    
    result = subprocess.run(['git', 'clone', repo_url, target_dir])
    
    if result.returncode == 0: 
        print(colored("téléchargement OK\n", "green"))
    else:
        print(colored("téléchargement KO\n", "red"))
    
    result = subprocess.run(['git', 'reset', '--hard', version], cwd=target_dir)
    
    if result.returncode == 0: 
        print(colored("branchement de version OK\n", "green"))
    else:
        print(colored("branchement de version KO\n", "red"))



def download_git_repos_from_file(file_path, target_dir):
    with open(file_path, 'r') as file:
        try:
            repos = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Erreur lors de la lecture du fichier YAML : {exc}")
            return

        if not isinstance(repos, list):
            print("Le fichier YAML doit contenir une liste de dépôts Git.")
            return

        for repo in repos:
            if 'name' not in repo or 'url' not in repo or 'version' not in repo:
                print("Champ 'name' ou 'url' ou 'version' manquant pour décrire la dépendance.")
                continue
            repo_name    = repo['name']
            repo_url     = repo['url']
            repo_version = repo['version']

            # Créer le répertoire cible s'il n'existe pas déjà
            os.makedirs(os.path.join(target_dir, repo_name), exist_ok=True)

            # Télécharger le dépôt Git
            download_git_repo(repo_url, os.path.join(target_dir, repo_name), repo_version)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script de téléchargement de dépôts Git à partir d\'un fichier YAML.')
    parser.add_argument('dir', help='Répertoire cible où télécharger les dépôts Git')
    parser.add_argument('file', help='Chemin du fichier YAML contenant la liste des dépôts Git')
    args = parser.parse_args()

    target_dir = args.dir
    file_path = args.file

    download_git_repos_from_file(file_path, target_dir)

