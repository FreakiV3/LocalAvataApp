import os
import vrchatapi
from vrchatapi import ApiException
from getpass import getpass
from requests import Request

def main():
    print("Bienvenue dans le script de connexion VRChat!")

    # Vérifie si le fichier AuthCookie existe et est valide
    auth_cookie_path = 'logs/AuthCookie.bin'
    if os.path.exists(auth_cookie_path):
        with open(auth_cookie_path, "r") as f:
            auth_cookie = f.read()

        configuration = vrchatapi.Configuration()
        configuration.api_key['cookie'] = auth_cookie

        try:
            with vrchatapi.ApiClient(configuration) as api_client:
                auth_api = vrchatapi.AuthenticationApi(api_client)
                current_user = auth_api.get_current_user()
                print("\033[92mConnecté en tant que:", current_user.display_name + "\033[0m")

                return True  # Si l'authentification réussit, on quitte la fonction
        except vrchatapi.ApiException as e:
            if "Invalid Username/Email or Password" in str(e):
                print("Nom d'utilisateur/Email ou mot de passe invalide. Veuillez réessayer.")
            else:
                print("Échec de l'authentification avec le cookie existant. Connexion requise.")

    try:
        # Invite l'utilisateur à entrer son nom d'utilisateur et son mot de passe
        username = input("Entrez votre nom d'utilisateur VRChat: ")
        password = getpass("Entrez votre mot de passe VRChat: ")

        configuration = vrchatapi.Configuration(
            username=username,
            password=password,
        )

        with vrchatapi.ApiClient(configuration) as api_client:
            auth_api = vrchatapi.AuthenticationApi(api_client)

            try:
                current_user = auth_api.get_current_user()
            except vrchatapi.ApiException as e:
                if "Invalid Username/Email or Password" in str(e):
                    print("Nom d'utilisateur/Email ou mot de passe invalide. Veuillez réessayer.")
                elif e.status == 200:
                    if "Email 2 Factor Authentication" in e.reason:
                        auth_api.verify2_fa_email_code(two_factor_email_code=vrchatapi.TwoFactorEmailCode(input("Code 2FA par email: ")))
                    elif "2 Factor Authentication" in e.reason:
                        two_factor_code = input("Code 2FA: ")
                        if two_factor_code:
                            auth_api.verify2_fa(two_factor_auth_code=vrchatapi.TwoFactorAuthCode(two_factor_code))
                        else:
                            print("L'authentification à deux facteurs est requise, mais aucun code n'a été fourni.")
                            return False
                    current_user = auth_api.get_current_user()
                else:
                    print("Exception lors de l'appel de l'API:", e)

            print("\033[92mConnecté en tant que:", current_user.display_name + "\033[0m")
            cookies = api_client.rest_client.cookie_jar
            mock_request_object = Request(url="https://api.vrchat.cloud/api/1/auth/user", method="GET")
            cookies.add_cookie_header(mock_request_object)
            auth_cookie = mock_request_object.get_header("Cookie")

            os.makedirs("logs", exist_ok=True)

            with open(auth_cookie_path, "wb") as f:
                f.write(auth_cookie.encode())
            print("Cookie d'authentification enregistré dans AuthCookie.bin")

            return True
    except Exception as e:
        print("Erreur lors de la connexion:", str(e))
        return False

def check_updates():
    # Désactivez la logique de vérification des mises à jour
    return {'update_available': False}

if __name__ == "__main__":
    main()
