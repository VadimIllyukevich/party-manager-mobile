import requests
import json
from kivy.app import App


class MyFirebase:
    wak = 'AIzaSyANjNBKpmYczNLYfJZyuJNYL8apAHGBJEM'  # Web Api Key

    def register(self, email, password):
        app = App.get_running_app()
        register_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=' + self.wak
        register_payload = {"email": email, "password": password, "returnSecureToken": True}
        register_request = requests.post(register_url, register_payload)
        register_data = json.loads(register_request.content.decode())

        if register_request.ok:
            refresh_token = register_data['refreshToken']
            localId = register_data['localId']
            idToken = register_data['idToken']
            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)

            # LocalId and IDToken
            app.local_id = localId
            app.id_token = idToken

            # Create new key in database
            my_data = '{"avatar": "images/fon_for_ mobile.jpg", "liked_establishment": ""}'
            post_request = requests.patch("https://party-manager-42e84-default-rtdb.firebaseio.com/users/" + localId +
                                          ".json?auth=" + idToken, data=my_data)
            print(post_request.ok)
            print(json.loads(post_request.content.decode()))
            app.change_screen("user_window")

        if not register_request.ok:
            error_data = json.loads(register_request.content.decode())
            error_message = error_data["error"]['message']
            App.get_running_app().root.ids['register_window'].ids['login_message'].text = error_message
        pass

    def exchange_refresh_token(self, refresh_token):
        refresh_url = "https://securetoken.googleapis.com/v1/token?key=" + self.wak
        refresh_payload = '{"grant_type": "refresh_token", "refresh_token": "%s"}' % refresh_token
        refresh_req = requests.post(refresh_url, data=refresh_payload)
        id_token = refresh_req.json()['id_token']
        local_id = refresh_req.json()['user_id']
        return id_token, local_id

    def sign_in(self):
        pass

