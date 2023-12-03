# modules/utils.py

from plyer import notification

def show_notification(message):
    notification.notify(
        title='VRCScannerTool',
        message=message,
        app_icon=None,  # Ajoutez ici le chemin vers l'icône si nécessaire
        timeout=10,
    )
