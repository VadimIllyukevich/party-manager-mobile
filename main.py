from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, CardTransition
from kivy.uix.label import Label
from myfirebase import MyFirebase
from banners import EstablishmentBanner, SnackBanner, BoozeBanner, LikedUserEstablishmentBanner
import requests
import json

Window.size = (480, 700)
Window.top, Window.left = (50, 200)


# Окна
class FirstWindow(Screen):
    pass


class BetweenSectionsWindow(Screen):
    pass


class BetweenSubsectionsReceptWindow(Screen):
    pass


class RegisterWindow(Screen):
    pass


class UserWindow(Screen):
    pass


class SignInWindow(Screen):
    pass


class BoozeListWindow(Screen):
    pass


class BoozePageWindow(Screen):
    pass


class EstablishmentListWindow(Screen):
    pass


class EstablishmentPageWindow(Screen):
    pass


class SnackListWindow(Screen):
    pass


class SnackPageWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# # Всплывающие окна
# class registerPopup(FloatLayout):
#     pass


# UI
class LabelButton(ButtonBehavior, Label):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


class ContainerForRegisterWindow(FloatLayout):
    pass


class ContainerForBetweenSubsectionsReceptWindow(BoxLayout):
    pass


class ContainerForFirstWindow(BoxLayout):
    pass


class ContainerForBetweenSectionsWindow(BoxLayout):
    pass


# Фон
class BackGroundImage(FloatLayout):
    pass


GUI = Builder.load_file("kivy.kv")


class ManagerApp(App):
    id = 1

    def build(self):
        self.my_firebase = MyFirebase()
        return GUI

    def change_screen(self, window_name):
        window_manager = self.root.ids['window_manager']
        window_manager.current = window_name

    # def show_popup(self):
    #     show = PopupRegister()
    #     popup_register = Popup(title='Register popup', content=show, size_hint=(0.8, 0.8))
    #     popup_register.open()

    def on_start(self):
        result = requests.get('https://party-manager-42e84-default-rtdb.firebaseio.com/.json')
        print("res ok?", result.ok)

        data = json.loads(result.content.decode())
        print(data)
        avatar_image = self.root.ids['user_window'].ids['avatar_image']
        avatar_image.source = "images/" + data['users']['1']['avatar']

        banner_grid_for_user = self.root.ids['user_window'].ids['banner_grid']
        liked_establishments_list = data['users']['1']['liked_establishment'][1:]
        for liked_establishment_list in liked_establishments_list:
            for i in range(5):
                liked_establishment_list_element = LikedUserEstablishmentBanner(
                    photo_establishment=liked_establishment_list['photo_establishment'],
                    descriptions=liked_establishment_list['descriptions'])
                banner_grid_for_user.add_widget(liked_establishment_list_element)

        # establishments list
        # banner_grid_for_establishment_list = self.root.ids['establishment_list_window'].ids['banner_grid_for_establishment_list']
        # establishments = data[''][1:]
        # for establishment in liked_establishments_list:
        #     establishment_list_element = EstablishmentBanner(
        #         photo=establishment['photo'],
        #         name=establishment['name'])
        #     banner_grid_for_establishment_list.add_widget(establishment_list_element)
        #
        # # booze list
        # banner_grid_for_booze_list = self.root.ids['establishment_list_window'].ids['banner_grid_for_list']
        # booze_list = data['users']['1']['liked_establishment'][1:]
        # for booze in booze_list:
        #     booze_list_element = EstablishmentBanner(photo_establishment=booze['photo_establishment'],
        #                                              descriptions=booze['descriptions'])
        #     banner_grid_for_booze_list.add_widget(booze_list_element)

        # snack list
        # banner_grid_for_snack_list = data['users'][1]['liked_establishment'][1:]
        # snack_list = self.root.ids['establishment_list_window'].ids['banner_grid_for_list']
        # for snack in snack_list:
        #     snack_list_element = SnackBanner(photo_establishment=snack['photo_establishment'],
        #                                      descriptions=snack['descriptions'])
        #     banner_grid_for_snack_list.add_widget(snack_list_element)


if __name__ == "__main__":
    ManagerApp().run()
