# modules/update.py

from modules.utils import show_notification
import requests
from packaging import version

def check_for_updates(current_version):
    try:
        # URL du fichier de version sur GitHub
        version_url = 'https://raw.githubusercontent.com/your_username/your_repository/main/version.txt'

        # Obtenir la version la plus récente depuis le fichier sur GitHub
        response = requests.get(version_url)
        latest_version_str = response.text.strip()
        latest_version = version.parse(latest_version_str)

        # Comparer les versions
        if latest_version > version.parse(current_version):
            # Il y a une mise à jour disponible
            show_notification(f'Nouvelle version disponible : {latest_version_str}')
            print(f'Nouvelle version disponible : {latest_version_str}')
            return True
        else:
            # La version est à jour
            print('La version est à jour.')
            return False

    except Exception as e:
        show_notification(f'Erreur lors de la vérification des mises à jour : {e}')
        print(f'Erreur lors de la vérification des mises à jour : {e}')
        return False
